from tortoise.models import Model
from tortoise import fields

class Article(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    desc = fields.CharField(max_length=255)
    content = fields.CharField(max_length=255)
    img = fields.CharField(max_length=255)
    link = fields.CharField(max_length=255)

    class Meta:
        table = "article"
        table_description = "articles"