from peewee import *
import datetime

db = SqliteDatabase('db.sqlite')

class BaseModel(Model):
    class Meta:
        database = db

class Product(BaseModel):
    name = TextField(unique=True)
    price = FloatField()
    category = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

def init_db():
    db.connect()
    db.create_tables([Product], safe=True)
    db.close()