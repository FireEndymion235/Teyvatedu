

from fastapi import FastAPI
from webcore.lifespan import app_lifespan
from fastapi.middleware.cors import CORSMiddleware
from webcore.endpoints import all_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from conf import config

app = FastAPI(lifespan=app_lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return RedirectResponse("/index.html")


app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ALLOW_ORIGINS,
    allow_credentials=config.CORS_ALLOW_CREDENTIALS,
    allow_methods=config.CORS_ALLOW_METHODS,
    allow_headers=config.CORS_ALLOW_HEADERS,
)

app.include_router(all_router)

