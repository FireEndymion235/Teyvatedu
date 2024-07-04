

# Datahub的生命周期管理

from fastapi import FastAPI
from tortoise import Tortoise
import contextlib
from conf import config
from .logcontroller import log
from .database import register_mysql
from os import walk
from libs.mail import send_email
from .dependencies import GlobalState, get_global_state
from pathlib import Path    
from .utils import get_system_info
def construct_webres():
    current_file_path = Path(__file__).parent.parent
    web_res_path = current_file_path.joinpath("webres")
    skip_files = []
    web_res = {}
    for _, _, i in walk(web_res_path):
        xmls = list(set(i) - set(skip_files))
        for xml in xmls:
            if xml.endswith(".xml"):
                # footer.xml
                with open(web_res_path.joinpath(xml), "r", encoding="utf-8") as f:
                    content = f.read()
                    # remove filename's .xml
                    tag = xml.split(".")[0]
                    web_res[tag] = content
        break

    return web_res

@contextlib.asynccontextmanager
async def app_lifespan(app: FastAPI):

    await register_mysql()

    state:GlobalState = get_global_state()
    state.runtime.set("webres",construct_webres())
    state.runtime.set("JWT_KEY",config.JWT_SECRET_KEY)
    state.runtime.set("JWT_DECRYPT",config.JWT_ALGORITHM)
    await send_email(config.LOG_EMAIL_SENDER,config.APP_NAME,f"APP starting: {app}",f"{config.APP_NAME} is starting up:{str(get_system_info())}")
    yield
    log.info(f"APP shutting down: {app}")
    await Tortoise.close_connections()
