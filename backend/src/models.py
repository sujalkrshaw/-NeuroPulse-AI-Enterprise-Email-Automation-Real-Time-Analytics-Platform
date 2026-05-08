from sqlalchemy import (
    Column,
    String,
    Boolean,
    Integer,
    DateTime,
    Text
)

from datetime import datetime

from src.database import Base

# -----------------------------------
# CONTACTS TABLE
# -----------------------------------

class Contact(Base):

    __tablename__ = "contacts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    email = Column(
        String,
        unique=True
    )

    department = Column(String)

    timezone = Column(String)

    unsubscribed = Column(
        Boolean,
        default=False
    )

# -----------------------------------
# REMINDERS TABLE
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

# -----------------------------------
# REAL EMAIL EVENTS TABLE
# -----------------------------------

class EmailEvent(Base):

    __tablename__ = "email_events"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    recipient_email = Column(String)

    subject = Column(String)

    status = Column(String)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )

    error_message = Column(
        Text,
        nullable=True
    )

    provider = Column(
        String,
        default="SMTP"
    )