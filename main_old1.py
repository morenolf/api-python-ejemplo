from fastapi import FastAPI, HTTPException
from peewee import SqliteDatabase, AutoField, TextField, DateField, ForeignKeyField, Model
from pydantic import BaseModel
from typing import Optional

app = FastAPI()




class Book(Model):
   codigo = TextField(primary_key=True)
   title = TextField()
   year = TextField()
   class Meta:
       database = db
       
class BookRequest(BaseModel):
   codigo: str
   title = str
   year = str

class SearchRequest(BaseModel):
    title: Optional[str] = None
    year: Optional[str] = None
   
db.create_tables([Book])

@app.post("/books")
def create_book(self, bookRequest: BookRequest):
        book = Book(codigo= bookRequest.codigo, title=bookRequest.title ,year=bookRequest.year)
        return book
   
@app.get("/books/{codigo}")
def get_book_by_id(self, codigo: str):
        book = Book().get(codigo=codigo)
        return book