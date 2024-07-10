from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.habit import Habit

from services.database_operations import create_habit_database
from configurations.database import get_database_session

router = APIRouter(
    prefix="/habits",
    tags=["habits"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_habits():
    return {"Response":"Hello from habits"}

@router.post("/create-habit")
async def create_habit_(habit:Habit, database: Session = Depends(get_database_session)):
    habitCreated = create_habit_database(database,habit)
    if habitCreated:
        return {"Response": "Habit created Successfully"}
    else:
        return {"Response" : "Error! Habit not created"}