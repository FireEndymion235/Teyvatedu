from tortoise.models import Model
from tortoise import fields
from pydantic import BaseModel
class Book(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    author = fields.CharField(max_length=255)
    desc = fields.CharField(max_length=255)
    content = fields.CharField(max_length=255)
    img = fields.CharField(max_length=255)
    link = fields.CharField(max_length=255)
    group = fields.CharField(max_length=255)
    class Meta:
        table = "book"
        table_description = "book"
        
class BookSchema(BaseModel):
    title:str
    author:str
    desc:str
    content:str
    img:str
    link:str
    group:str