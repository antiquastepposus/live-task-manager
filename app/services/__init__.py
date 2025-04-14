from app.utils.unitofwork import UserUnitOfWork, TaskUnitOfWork
from app.api.schemas.task import TaskCreate, TaskFromDB
from app.api.schemas.user import UserCreate, UserFromDB
from pydantic import BaseModel
from app.exceptions.exceptions import TaskNotFoundError