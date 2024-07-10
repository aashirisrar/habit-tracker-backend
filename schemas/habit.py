from pydantic import BaseModel

class Habit(BaseModel):
    id: int
    title: str
    details: str
    ownerid: int

class Config:
    orm_mode = True