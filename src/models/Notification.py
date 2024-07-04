from tortoise.models import Model
from tortoise import fields
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class Notification(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    desc = fields.CharField(max_length=255)
    content = fields.CharField(max_length=255)
    img = fields.CharField(max_length=255)
    link = fields.CharField(max_length=255)
    datetime = fields.DatetimeField(auto_now_add=True)
    publish = fields.CharField(max_length=255,default="出版社官方")
    expire_time = fields.DatetimeField(null=True)

    class Meta:
        table = "notification"
        table_description = "notifications"

        
class NotificationSchema(BaseModel):
    title:str
    desc:Optional[str] = None
    content:str
    img:Optional[str]=None
    link:Optional[str] = None
    datetime:Optional[datetime]
    publish:Optional[str] = "出版社官方"
    expire_time:Optional[datetime]