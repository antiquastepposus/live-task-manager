from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from app.db.models import User, Task 
from app.api.schemas.user import UserCreate
from abc import ABC, abstractmethod