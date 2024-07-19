from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import List

from datetime import timedelta

from schemas.user import UserCreate
from models.user import User
from models.habit import Habit
from models.value import Value
from configurations.token_configuration import ACCESS_TOKEN_EXPIRY_MINUTE, create_access_token, decoded_access_token
from utilities.user import verify_password, hash_password

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

def get_habit_with_id_database(database: Session, habitId):
    query = text(f"SELECT * FROM habits where id={habitId}")
    result = database.execute(query)
    return result.mappings().first()

def create_values_database(database: Session, value: Value):
    database_value = Value(habit_id=value.habit_id, date=value.date, count=value.count)
    database.add(database_value)
    database.commit()
    database.refresh(database_value)
    return database_value

def get_habit_valuesDatabase_database(database: Session, habitId) -> List[Value]:
    query = text(f"SELECT * FROM values where habit_id={habitId}")
    result = database.execute(query)
    return result.mappings().all()

def delete_habit_with_id_database(database: Session, habitId):
    query = text(f"DELETE FROM habits where id={habitId}")
    database.execute(query)
    database.commit()
    return True

# user signup
def create_user_service(database: Session, user: UserCreate):
    query = text(f"SELECT id FROM users WHERE email='{user.email}'")
    result = database.execute(query)
    user_in_database = result.mappings().first()

    if user_in_database:
        return {"error": "user already exists"}
    
    hashed_password = hash_password(user.password)
    user.password = hashed_password

    database_user = User(email=user.email, hashed_password=user.password)
    database.add(database_user)
    database.commit()
    database.refresh(database_user)
    return database_user

# user authentication
def validate_user(database: Session, userCreated: UserCreate):
    query = text(f"SELECT * FROM users WHERE email='{userCreated.email}'")
    result = database.execute(query)
    user = result.mappings().first()
    print(user)

    if user and verify_password(userCreated.password, user['hashed_password']):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTE)
        access_token = create_access_token(data={"mail": user["email"],"id": user["id"]}, expires_delta=access_token_expires)
        # decoded = decoded_access_token(access_token)
        print(access_token)
        return { "access_token": access_token, "token_type": "bearer", "id": user["id"],  "email": user["email"]}
    else:
        return None