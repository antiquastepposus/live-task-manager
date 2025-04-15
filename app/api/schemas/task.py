from typing import Optional
from . import BaseModel, Field, ConfigDict, datetime    

class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=30)
    description: Optional[str] = Field(default=None, max_length=1000)

class TaskFromDB(TaskCreate):
    id: int
    completed: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }