

# Datahub的生命周期管理

from fastapi import FastAPI
from tortoise import Tortoise
import contextlib
from conf import config
from .logcontroller import log
from os import path, makedirs, walk
from .dependencies import GlobalState, get_global_state
from pathlib import Path    
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

    folder = path.join(*config.SQLITE_DIR)
    # [LIFESPAN 01] 初始化SQLite数据库
    # if folder is not exist, create it
    if not path.exists(folder):
        log.info(f"SQLite database folder not found, creating folder {folder}")
        makedirs(folder)

    config_dict = {
        "connections": {
            "default": {
                "engine": "tortoise.backends.sqlite",
                "credentials": {
                    "file_path": config.SQLITE_URL
                }
            }
        },
        "apps": {
            "models": {
                "models": config.SQLITE_MODELS,
                "default_connection": "default"
            }
        }
    }
    
    await Tortoise.init(
        config=config_dict
    )
    await Tortoise.generate_schemas()
    log.info(f"generating models:{config.SQLITE_MODELS}")
    log.info("SQLite database initialized")
    state:GlobalState = get_global_state()
    state.runtime.set("webres",construct_webres())
    yield
    log.info(f"APP shutting down: {app}")
    await Tortoise.close_connections()
