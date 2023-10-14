import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from routes import file
from utils import is_not_env_exist

# Load env in dev-mode (directly run main.py in ./api dir)
# 직접적으로 개발 환경에서 main.py를 실행하는 경우
# .env 파일의 환경변수를 불러옴
is_not_env_exist(load_dotenv)

# 만약 docker-compose로 실행 한 경우 이미 환경변수가 존재하기에
# load_dotenv()가 필요하지 않으므로 그냥 확인함
is_not_env_exist()

if not os.path.exists(f"..{file.SAFE_DIR}"):
    os.mkdir(f"..{file.SAFE_DIR}")

app = FastAPI()

app.include_router(file.router, prefix="/file", tags=["file"])


@app.get("/")
def root():
    return {"message": "StarSafe is running!"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=1777, reload=True)
