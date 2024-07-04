from tortoise.models import Model
from tortoise import fields

class Access(Model):
    id = fields.IntField(pk=True)
    endpoint = fields.CharField(max_length=255)
    ip = fields.CharField(max_length=255)
    user = fields.CharField(max_length=255)

    class Meta:
        table = "access"
        table_description = "Access log"