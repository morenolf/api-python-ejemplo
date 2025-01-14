from fastapi import FastAPI
from users_router import users_router

app = FastAPI()

app.include_router(users_router)
