from . import APIRouter

users_router = APIRouter(
    prefix="/users",
    tags=["users"]
)