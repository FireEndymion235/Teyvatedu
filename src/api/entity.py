from fastapi import APIRouter,Security

from models.Notification import Notification,NotificationSchema
from models.Book import Book,BookSchema
from webcore.authorize import check_permissions
import os
backend_router = APIRouter(prefix="/api/v1",tags=["Ressources"],dependencies=[Security(check_permissions,scopes=["admin"])])
async def delete_static_image(img:str):
    if img:
        if os.path.exists(f"static/images/{img}"):
            os.remove(f"static/images/{img}")


# CURD for notifications
@backend_router.post("/notification")
async def post_notification(notification: NotificationSchema):
    await Notification.create(**notification.model_dump())
    return {"status":"ok"}
@backend_router.get("/notification")
async def get_notification():
    return await Notification.all()

@backend_router.get("/notification/{id}")
async def get_notification_byId(id:int):
    return await Notification.filter(id=id).first()

@backend_router.delete("/notification/{id}")
async def delete_notification(id:int):
    note = await Notification.filter(id=id).first()
    delete_static_image(note.img)
    await note.delete()
    return {"status":"ok"}

# CURD for books
@backend_router.post("/book")
async def post_book(book: BookSchema):
    await Book.create(**book.model_dump())
    return {"status":"ok"}

@backend_router.get("/book")
async def get_book():
    return await Book.all()

@backend_router.get("/book/{id}")
async def get_book_byId(id:int):
    return await Book.filter(id=id).first()

@backend_router.delete("/book/{id}")
async def delete_book(id:int):
    book = await Book.filter(id=id).first()
    delete_static_image(book.img)
    await book.delete()
    return {"status":"ok"}


@backend_router.get("/resources")
async def get_all_resources():
    # get all files in static/images and static/pdfs
    images = os.listdir("static/images")
    pdfs = os.listdir("static/pdfs")
    return {
        "images": images,
        "pdfs": pdfs
    }

@backend_router.delete("/resouce/{path}/{filename}")
async def delete_resource(path:str,filename:str):
    if os.path.exists(f"static/{path}/{filename}"):
        os.remove(f"static/{path}/{filename}")
    return {"status":"ok"}
