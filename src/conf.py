

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field
from typing import List
from os import path,walk

def get_models() -> list:
    """
    获取model文件夹下的文件 即需要注册到MySQL的Model
    :return:
    """
    skip_files = ['Basic.py', '__init__.py']
    ret = []
    for _, _, i in walk(path.join("models")):
        models = list(set(i) - set(skip_files))
        for model in models:
            model = model.replace(".py", "")
            model = "models." + model
            ret.append(model)
        break

    return ret

load_dotenv()

class AppConfig(BaseSettings):

    # Basic info for app's OpenAPI schema
    APP_NAME:str = Field(default="Backend", env="APP_NAME",description="提瓦特教育出版社API")
    APP_VERSION:str = Field(default="0.0.1", env="APP_VERSION",description="0.1.0")
    APP_TITLE:str = Field(default="RPICS", env="APP_TITLE",description="提瓦特教育出版社API")
    APP_DESCRIPTION:str = Field(default="The backend for RPICS", env="APP_DESCRIPTION",description="提瓦特教育出版社API后台管理页面")
    APP_DEBUG:bool = Field(default=True, env="APP_DEBUG",description="APP调试模式")

    # -------------------- JWT --------------------
    # JWT (Json Web Token) 
    JWT_SECRET_KEY: str = Field(default="randomkey",env="JWT_SECRET_KEY",description="JWT密钥")
    JWT_ACCESS_EXPIRE_MINUTES: int = Field(default=24*60,env="JWT_ACCESS_EXPIRE_MINUTES",description="JWT过期时间")
    JWT_ALGORITHM: str = Field(default="HS256",env="JWT_ALGORITHM",description="JWT算法")
    # -------------------- CORS --------------------
    # Cross-Origin Resource Sharing Policy
    CORS_ALLOW_ORIGINS: List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List = ["*"]
    CORS_ALLOW_HEADERS: List = ["*"]
    # -------------------- SQLite --------------------
    # SQLite config for tortoise ORM
    SQLITE_DIR: List = [".","sqlite3"]
    SQLITE_FILE: str = "tep.db"
    SQLITE_URL: str = path.join(*SQLITE_DIR,SQLITE_FILE)
    SQLITE_MODELS: list = get_models()

    

config = AppConfig()
