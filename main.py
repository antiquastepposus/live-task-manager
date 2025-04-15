import asyncio
from fastapi import FastAPI, websockets
from app.api.endpoints.tasks import tasks_router
from app.api.endpoints.users import users_router
from app.api.endpoints.websocket import websocket_router

app = FastAPI()
app.include_router(tasks_router)
app.include_router(users_router)
app.include_router(websocket_router)