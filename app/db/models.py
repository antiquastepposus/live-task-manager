from datetime import datetime
from sqlalchemy import BigInteger, DateTime, String, func, ForeignKey
from . import Mapped, mapped_column
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(16), index=True, unique=True)
    password: Mapped[str] = mapped_column(String(255))

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(1000), default=None, nullable=True)
    completed: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, 
                                    server_default=func.now())
    
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)