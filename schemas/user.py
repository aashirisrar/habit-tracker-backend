from pydantic import BaseModel
from .habit import Habit

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    habits: list[Habit] = []

    class Config:
        orm_mode = True