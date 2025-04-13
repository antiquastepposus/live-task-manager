from . import BaseModel, Field, ConfigDict, datetime    

class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=30)
    description: str = Field(default=None, min_length=5, max_length=1000)

class TaskFromDB(TaskCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    completed: bool
    created_at: datetime