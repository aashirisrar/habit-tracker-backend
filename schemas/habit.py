from pydantic import BaseModel

class Habit(BaseModel):
    id: int
    title: str
    details: str

class Config:
    orm_mode = True