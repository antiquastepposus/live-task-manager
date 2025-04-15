from app.utils.unitofwork import UserUnitOfWork, TaskUnitOfWork
from app.api.schemas.task import TaskCreate, TaskFromDB
from app.api.schemas.user import UserCreate, UserFromDB
from app.exceptions.exceptions import TaskNotFoundError, UserNotFoundError, WrongCredentialsError, UsernameAlreadyExists
from app.core.security import get_password_hash, verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta