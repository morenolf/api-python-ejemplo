from fastapi import APIRouter
from pydantic import BaseModel
from models import User

users_router = APIRouter()

class UserRequest(BaseModel):
    username: str
    email: str
    
@users_router.post("/users")
def create_book(userRequest: UserRequest):
        user = User(username= userRequest.username, email=userRequest.email)
        user.save()
        return user