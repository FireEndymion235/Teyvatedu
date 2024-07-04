

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
    APP_VERSION:str = Field(default="0.1.0", env="APP_VERSION",description="0.1.0")
    APP_TITLE:str = Field(default="TEP", env="APP_TITLE",description="提瓦特教育出版社API")
    APP_DESCRIPTION:str = Field(default="The backend for RPICS", env="APP_DESCRIPTION",description="提瓦特教育出版社API后台管理页面")
    APP_DEBUG:bool = Field(default=False, env="APP_DEBUG",description="APP调试模式")

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
    # -------------------- ENV Shows --------------------
    ES: str = Field(default="Default",env="ES",description="JWT过期时间")

    # -------------------- MYSQL --------------------
    # MySQL config for tortoise ORM
    MYSQL_HOST:str = Field(default="localhost", env="MYSQL_HOST",description="MySQL主机地址")
    MYSQL_PORT:int = Field(default=3306, env="MYSQL_PORT",description="MySQL端口")
    MYSQL_USER:str = Field(default="root", env="MYSQL_USER",description="MySQL用户名")
    MYSQL_PASS:str = Field(default="123456", env="MYSQL_PASS",description="MySQL密码")
    MYSQL_DB:str = Field(default="tep", env="MYSQL_DB",description="MySQL数据库名称")
    GLOBAL_TIMEZONE: str = Field(default="Asia/Shanghai", env="GLOBAL_TIMEZONE",description="全局时区")
    MYSQL_TEST_TABLE: str = Field(default="files",env="MYSQL_TEST_TABLE",description="JWT过期时间")

    # -------------------- MAIL --------------------
    STMP_SERVER: str = Field(default="smtp.163.com", env="STMP_SERVER",description="SMTP服务器")
    STMP_USER: str = Field(default="<EMAIL>", env="STMP_USER",description="SMTP用户名")
    STMP_PASS: str = Field(default="<PASSWORD>", env="STMP_PASS",description="SMTP密码")
    STMP_SWITCH: bool = Field(default=True, env="STMP_SWITCH",description="SMTP开关")
    LOG_EMAIL_SENDER: str = Field(default="<EMAIL>", env="LOG_EMAIL_SENDER",description="SMTPCit")

config = AppConfig()
