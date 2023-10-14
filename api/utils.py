import os
from typing import Optional, Callable


def is_not_env_exist(
        execute: Optional[Callable] = None,
        envs=("PW", "SAFE_DIR")
):
    # if missing something in env, exit
    for e in envs:
        if os.getenv(e) is None:
            print(f"Please set the {e} environment variable.")
            print("If you in development, you need to check the .env file.")
            exit(1)
    # if everything is ok, execute
    execute()
