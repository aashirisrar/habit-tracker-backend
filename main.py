from fastapi import FastAPI, APIRouter
from typing import Union

from routers import users, habits

app = FastAPI()

app.include_router(users.router)
app.include_router(habits.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
