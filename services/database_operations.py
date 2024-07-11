from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import List

from schemas.user import UserCreate
from models.user import User
from models.habit import Habit

def create_user_database(database: Session, user: UserCreate):
    fake_hashed_password = user.password
    database_user = User(email=user.email, hashed_password=fake_hashed_password)
    database.add(database_user)
    database.commit()
    database.refresh(database_user)
    return database_user

def create_habit_database(database: Session, habit: Habit):
    database_habit = Habit(title = habit.title, details= habit.details, owner_id = habit.owner_id)
    database.add(database_habit)
    database.commit()
    database.refresh(database_habit)
    return database_habit

def get_habits_database(database: Session, userId) -> List[Habit]:
    query = text(f"SELECT * FROM habits where owner_id={userId}")
    result = database.execute(query)
    return result.mappings().all()