from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from configurations.database import get_database_session
from services.database_operations import create_user_database
from schemas.user import UserCreate

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def user_read():
    return {"Response":"Hello from users"}

@router.post("/create-user")
async def create_user_(user:UserCreate, database: Session = Depends(get_database_session)):
    userCreated = create_user_database(database,user)
    if userCreated:
        return {"Response": "User created Successfully"}
    else:
        return {"Response" : "Error! User not created"}