
from peewee import SqliteDatabase, Model
from peewee import SqliteDatabase, TextField, Model

db = SqliteDatabase('library.db')

class ORMBaseModel(Model):
   class Meta:
       database = SqliteDatabase('library2.db')

class User(ORMBaseModel):
   username = TextField()
   email = TextField()
   class Meta:
       db_table = 'Users'
       
db.connect()
db.create_tables([User])