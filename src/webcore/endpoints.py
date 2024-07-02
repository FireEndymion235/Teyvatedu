
from fastapi import APIRouter
from api import htmls


all_router = APIRouter()

all_router.include_router(htmls.html_router)