from fastapi import APIRouter

users_router = APIRouter(prefix="/users")

@users_router.get("/")
async def get_users():
    return [{"username": "Rick"}, {"username": "Morty"}]