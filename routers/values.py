from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from configurations.database import get_database_session
from services.database_operations import create_values_database, get_habit_valuesDatabase_database
from schemas.value import Values

router = APIRouter(
    prefix="/values",
    tags=["values"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def values_read():
    return {"Response":"Hello from values"}

@router.post("/create-values")
async def create_values_(values:Values, database: Session = Depends(get_database_session)):
    valuesCreated = create_values_database(database,values)
    if valuesCreated:
        return {"Response": "Values created Successfully"}
    else:
        return {"Response" : "Error! Values not created"}
    
@router.post("/get-habit-values")
async def get_habit_values_(habitId, database: Session = Depends(get_database_session)):
    valuesDatabase = get_habit_valuesDatabase_database(database,habitId)
    if valuesDatabase is None:
        return {"Response" : "Error! No values found"}
    else:
        return {"Response" : "Values found", "values":valuesDatabase}