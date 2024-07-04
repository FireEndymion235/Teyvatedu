from tortoise.models import Model
from tortoise import fields
from pydantic import BaseModel
class File(Model):
    id = fields.IntField(pk=True)
    filename = fields.CharField(max_length=255)
    fileowner = fields.CharField(max_length=255,default="sys")
    path = fields.CharField(max_length=255)
    filename_hash = fields.CharField(max_length=255)

    class Meta:
        table = 'files'
        table_description = 'File table'

class FileSchema(BaseModel):
    filename: str
    path: str
    filename_hash: str