from fastapi import FastAPI
from controller.users.users_controller import *
from service.users.users_service import *
from repository.users.users_repository import *

app = FastAPI()

users_repository = UsersRepository()
users_service = UsersService(users_repository)
init_users_controller()

app.include_router(users_router)