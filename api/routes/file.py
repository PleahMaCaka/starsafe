import os
import shutil

from fastapi import APIRouter, HTTPException
from fastapi import File, UploadFile
from fastapi.responses import FileResponse

PASSWORD = os.getenv("PW")
SAFE_DIR = os.getenv("SAFE_DIR")

router = APIRouter()


def check_password(pw: str):
    if pw != PASSWORD:
        raise HTTPException(status_code=401, detail="Incorrect password")


@router.post("/upload")
async def upload_file(pw: str, file: UploadFile = File(...)):
    check_password(pw)

    with open(f"..{SAFE_DIR}/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "File upload successful"}


@router.get("/")
async def list_files(pw: str):
    check_password(pw)

    files = os.listdir(f"..{SAFE_DIR}")

    if not files:
        raise HTTPException(status_code=404, detail="Safe is empty")

    return {"files": files}


@router.get("/download")
async def download_file(pw: str, file_name: str):
    check_password(pw)

    file_path = f"../safe/{file_name}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(path=file_path)
