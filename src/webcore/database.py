\
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import re
from conf import config,get_models
from pymysql import connect
from .logcontroller import log
from typing import Dict
from tortoise import Tortoise
from os import path, makedirs, walk
def execute_sql_query(sql_query: str):
    with connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASS,
        port=config.MYSQL_PORT,
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_query)
            conn.commit()
            return cursor.fetchall()


def execute_mysql_query(sql_query: str) -> None:
    log.debug(f"[MYSQL RAW] executing sql: {sql_query}")
    with connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASS,
        port=config.MYSQL_PORT,
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql_query)
            conn.commit()


async def mysql_connect_test()->Dict[str,bool]:
    result_state = {
        "generate_schemas": False,  # table not exists
        "create_database": False,  # database not exists
    }
        # there are following situations:
        # 1. No Database: error code is 1049
        # 2. No Table: error code is 1146
    try:
        sql_query = f"USE {config.MYSQL_DB};"
        execute_mysql_query(sql_query)
    except Exception as e:
        log.error(f"[MYSQL 1049] Error {e}")
        # create database and build schema
        result_state["create_database"] = True
        result_state["generate_schemas"] = True
        return result_state
    try:
        sql_query = f"SELECT * FROM {config.MYSQL_DB}.{config.MYSQL_TEST_TABLE};"
        execute_mysql_query(sql_query)
        log.debug("[MYSQL RAW] Executing SQL query:" + sql_query)
    except Exception as e:
        # example: (1007, "Can't create database 'xxx'; database exists")
        # use the regex to get the error code
        error_code = re.findall(r"\((\d+)\,", str(e))[0]
        log.error(f"[MYSQL {error_code}] Error {e}")
        result_state['generate_schemas'] = True
        result_state['create_database'] = False
    return result_state


async def register_mysql():
    """
    注册mysql数据库 自动建表 从config中读取信息
    :param app:
    :return:
    """
    models = get_models()
    config_dict = {
        "connections": {
            "default": {  # base database named base
                'engine': 'tortoise.backends.mysql',
                "credentials": {
                    'host': config.MYSQL_HOST,
                    'user': config.MYSQL_USER,
                    'password': config.MYSQL_PASS,  # password of mysql server
                    'port': config.MYSQL_PORT,
                    'database': config.MYSQL_DB,  # name of mysql database server
                }
            },
        },
        "apps": {
            "models": {
                "models": models,  # model file in ./models
                "default_connection": "default"  # link to `base` database
            },
        },
        'use_tz': True,
        'timezone': config.GLOBAL_TIMEZONE
    }
    
    test_result = await mysql_connect_test()
    await Tortoise.init(
        config=config_dict,
        _create_db=test_result["create_database"]
    )
    if test_result["generate_schemas"]:
        await Tortoise.generate_schemas()
    """
        register_tortoise(
        app,
        config=config_dict,
    #    modules={"models": models},
        generate_schemas=test_result["generate_schemas"],
        add_exception_handlers=config.APP_DEBUG,
    )
    """

    
    log.info("[MySQL CNN] MySQL registered")


async def register_sqlite():
    
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