from . import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=30)
    description: str = Field(default=None, min_length=5, max_length=1000)
