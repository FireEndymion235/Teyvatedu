
from fastapi import APIRouter
from api import htmls
from api import entity
from api import file
from api import secure
all_router = APIRouter()

all_router.include_router(htmls.html_router)
all_router.include_router(entity.backend_router)
all_router.include_router(secure.secure_router)
all_router.include_router(file.file_router)