from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/habits",
    tags=["habits"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_habits():
    return {"Response":"Hello from habits"}

@router.post("/create_habit")
async def create_habit_(habit):
    habitCreated = create_habit_database(habit)
    if habitCreated:
        return {"Response": "Habit created Successfully"}
    else:
        return {"Response" : "Error! Habit not created"}