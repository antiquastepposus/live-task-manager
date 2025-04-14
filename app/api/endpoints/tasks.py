from . import APIRouter

tasks_router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)