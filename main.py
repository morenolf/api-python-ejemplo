from fastapi import FastAPI, APIRouter
from controller.users_controller import users_router

app = FastAPI()

app.include_router(users_router, prefix="/api")