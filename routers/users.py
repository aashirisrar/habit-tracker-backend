from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def user_read():
    return {"Response":"Hello from users"}
