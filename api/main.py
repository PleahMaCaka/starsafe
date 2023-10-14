import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()

# app.include_router(file.router, prefix="/file", tags=["file"])

PW = os.getenv("PW")


@app.get("/")
def root():
    return {"message": "StarSafe is running!"}


@app.get("/pw")
def get_pw():
    return {"pw": PW}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
