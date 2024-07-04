from tortoise.models import Model
from tortoise import fields

class File(Model):
    id = fields.IntField(pk=True)
    filename = fields.CharField(max_length=255, unique=True)
    fileowner = fields.CharField(max_length=255)
    path = fields.CharField(max_length=255)
    filename_hash = fields.CharField(max_length=255)

    class Meta:
        table = 'files'
        table_description = 'File table'