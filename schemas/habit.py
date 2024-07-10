from pydantic import BaseModel

class Habit(BaseModel):
    title: str
    details: str
    owner_id: int

class HabitCreate(Habit):
    id: int

class Config:
    orm_mode = True