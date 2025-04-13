from . import BaseModel, Field

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=16)
    password: str = Field(min_length=6, max_length=16)