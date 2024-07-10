from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from ..configurations import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    habits = relationship("Habit", back_populates="owner")

class Habits(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    details = Column(String)
    

