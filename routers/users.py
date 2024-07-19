from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from configurations.database import get_database_session
from services.database_operations import create_user_service, validate_user
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
async def create_user(user:UserCreate, database: Session = Depends(get_database_session)):
    new_user = create_user_service(database,user)
    return new_user

@router.post("/user-login")
def login_validation(user: UserCreate, database: Session = Depends(get_database_session)):
    validated_user = validate_user(database, user)
    return validated_user