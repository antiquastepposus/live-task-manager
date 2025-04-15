from . import BaseModel, Field, ConfigDict

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=16)
    password: str = Field(min_length=6, max_length=255)

class UserFromDB(UserCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int