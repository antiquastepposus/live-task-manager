from pydantic_settings import BaseSettings
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta, datetime, timezone
from fastapi import Depends, HTTPException, status
import jwt

from app.utils.unitofwork import UserUnitOfWork