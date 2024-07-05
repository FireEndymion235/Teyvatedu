from fastapi import APIRouter,Security
from fastapi import UploadFile
from fastapi.responses import FileResponse
from webcore.utils import random_string
from fastapi import HTTPException
from webcore.authorize import check_permissions
from aiofiles import open
from loguru import logger
from models import Files

file_router = APIRouter(prefix="/api/v1",tags=["File"],dependencies=[Security(check_permissions,scopes=["admin"])])
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
    await Files.File.create(filename=file.filename,path=f"static/images/{new_filename}",filename_hash=new_filename)
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
    await Files.File.create(filename=file.filename,path=f"static/pdfs/{new_filename}",filename_hash=new_filename)
    return {"filename": new_filename}

@file_router.get("/get/image/{filename}")
async def download_image(filename: str):
    try:
        resp = FileResponse(f"static/images/{filename}")
    except Exception as e:
        logger.error(e)
        return HTTPException(status_code=404, detail="File not found")
    return resp

@file_router.get("/get/pdf/{filename}")
async def download_pdf(filename: str):
    try:
        resp = FileResponse(f"static/pdfs/{filename}")
    except Exception as e:
        logger.error(e)
        return HTTPException(status_code=404, detail="File not found")
    return resp

@file_router.get("/files")
async def get_all_files():
    files = await Files.File.all()
    return files