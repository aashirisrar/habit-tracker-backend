from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from configurations.database import Base

class Value(Base):
    __tablename__ = "values"

    id = Column(Integer,  primary_key=True)
    date = Column(String)
    count = Column(String)
    habit_id = Column(Integer, ForeignKey("habits.id"))

    ownerHabit = relationship("Habit", back_populates="values")