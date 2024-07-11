from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.habit import Habit

from services.database_operations import create_habit_database,get_habits_database, get_habit_with_id_database
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
    
@router.post("/get-user-habits")
async def get_habits_(userId, database: Session = Depends(get_database_session)):
    habits = get_habits_database(database,userId)
    if habits is None:
        return {"Response" : "Error! No habits found"}
    else:
        return {"Response" : "Habits found", "habits":habits}

@router.post("/get-habit")
async def get_habits_(habitId, database: Session = Depends(get_database_session)):
    habits = get_habit_with_id_database(database,habitId)
    if habits is None:
        return {"Response" : "Error! No habits found"}
    else:
        return {"Response" : "Habit found", "habits":habits}