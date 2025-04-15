from fastapi import FastAPI
from app.api.endpoints.tasks import tasks_router
from app.api.endpoints.users import users_router

app = FastAPI()
app.include_router(tasks_router)
app.include_router(users_router)