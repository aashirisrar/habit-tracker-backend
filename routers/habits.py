from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/habits",
    tags=["habits"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_habits():
    return {"Response":"Hello from habits"}
