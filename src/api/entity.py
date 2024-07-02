from fastapi import APIRouter
from models.Notification import Notification,NotificationSchema
from models.Book import Book,BookSchema
backend_router = APIRouter(prefix="/api/v1")


# CURD for notifications
@backend_router.post("/notification")
async def post_notification(notification: NotificationSchema):
    await Notification.create(**notification.model_dump())
    return {"status":"ok"}

# CURD for books
@backend_router.post("/book")
async def post_book(book: BookSchema):
    await Book.create(**book.model_dump())
    return {"status":"ok"}

