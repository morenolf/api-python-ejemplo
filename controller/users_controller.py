from fastapi import APIRouter

users_router = APIRouter(prefix="/users")

user = [{"username": "Rick"}, {"username": "Morty"}]

@users_router.get("/")
async def get_users():
    return user