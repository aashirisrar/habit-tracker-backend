from pydantic import BaseModel

class Values(BaseModel):
    date: str
    count: int
    habit_id: int


class ValuesCreate(Values):
    id: int

class Config:
    orm_mode = True