from tortoise.models import Model
from tortoise import fields

class File(Model):
    filename = fields.CharField(max_length=50, unique=True)
    fileowner = fields.CharField(max_length=50)

