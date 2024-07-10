from sqlalchemy.orm import Session
from schemas.user import UserCreate
from models.user import User
from models.habit import Habit

def create_user_database(db: Session, user: UserCreate):
    fake_hashed_password = user.password
    db_user = User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_habit_database(db: Session, habit: Habit):
    db_habit = Habit(id=habit.id, title = habit.title, details= habit.details)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit