from tortoise import fields, Tortoise
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    telegram_id = fields.BigIntField(unique=True)
    username = fields.CharField(max_length=255, null=True)
    first_name = fields.CharField(max_length=255, null=True)
    last_name = fields.CharField(max_length=255, null=True)
    requests = fields.ReverseRelation["Request"]
    balance = fields.IntField(default=15)


class Request(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="user_requests")
    timestamp = fields.DatetimeField(auto_now_add=True)
    query = fields.TextField()
    token = fields.TextField()


class Response(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='response_logs')
    response_data = fields.TextField(null=True)
    created_at = fields.DatetimeField(auto_now_add=True)


async def initialize():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['gemini_bot.models']}
    )
    await Tortoise.generate_schemas()
