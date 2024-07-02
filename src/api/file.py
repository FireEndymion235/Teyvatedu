from fastapi import APIRouter
from fastapi import File, UploadFile
from fastapi.responses import FileResponse
from webcore.utils import random_string
from fastapi import HTTPException
from aiofiles import open
from loguru import logger
from base64 import b64encode, b64decode
file_router = APIRouter(prefix="/api/v1")
allowed_extensions = ['.jpg', '.jpeg', '.png', '.gif']
@file_router.post("/image/upload")
async def upload_file(file: UploadFile):
    logger.debug(file)
    filename = file.filename
    file_extension = '.' + filename.split('.')[-1].lower()
    logger.debug(filename)
    logger.debug(file_extension)
    if file_extension not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Invalid image file")

    random_filename = await random_string()
    new_filename = random_filename + file_extension
    logger.debug(new_filename)
    async with open(f"static/images/{new_filename}", 'wb') as buffer:
        while chunk := await file.read(1024):
            await buffer.write(chunk)
    return {"filename": new_filename}

@file_router.post("/pdf/upload")
async def upload_pdf(file:UploadFile):
    filename = file.filename
    file_extension = '.' + filename.split('.')[-1].lower()
    if file_extension != '.pdf':
        raise HTTPException(status_code=400, detail="Invalid pdf file")
    random_filename = await random_string()
    new_filename = random_filename + file_extension
    async with open(f"static/pdfs/{new_filename}", 'wb') as buffer:
        while chunk := await file.read(1024):
            await buffer.write(chunk)
    return {"filename": new_filename}

@file_router.get("/image/{filename}")
async def download_image(filename: str):
    return FileResponse(f"static/images/{filename}")

@file_router.get("/pdf/{filename}")
async def download_pdf(filename: str):
    return FileResponse(f"static/pdfs/{filename}")
