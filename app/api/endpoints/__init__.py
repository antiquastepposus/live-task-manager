from fastapi import APIRouter, Depends, HTTPException, status
from app.api.schemas.user import UserCreate
from app.services.user_service import UserService
from app.dependencies.dependencies import get_user_service 
from app.exceptions.exceptions import TaskNotFoundError, WrongCredentialsError, UserNotFoundError