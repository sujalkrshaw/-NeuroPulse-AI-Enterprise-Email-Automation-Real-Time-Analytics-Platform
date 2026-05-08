from sqlalchemy import Column, Integer, String
from database import Base

# -----------------------------------
# CONTACT TABLE
# -----------------------------------

class Contact(Base):

    __tablename__ = "contacts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    email = Column(String)

    department = Column(String)

    timezone = Column(String)

# -----------------------------------
# REMINDER TABLE
# -----------------------------------

class Reminder(Base):

    __tablename__ = "reminders"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    email = Column(String)

    reminder_type = Column(String)

    schedule_time = Column(String)

    template_name = Column(String)

    recurring = Column(String)