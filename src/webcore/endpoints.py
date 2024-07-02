
from fastapi import APIRouter
from api import htmls
from api import entity

all_router = APIRouter()

all_router.include_router(htmls.html_router)
all_router.include_router(entity.backend_router)