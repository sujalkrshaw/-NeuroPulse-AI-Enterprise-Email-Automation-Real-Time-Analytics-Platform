from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy import DateTime, Text
from src.database import Base

# -----------------------------
# CONTACTS TABLE
# -----------------------------

class Contact(Base):

    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)
    email = Column(String, unique=True)

    department = Column(String)

    timezone = Column(String)

    unsubscribed = Column(Boolean, default=False)


# -----------------------------
# REMINDERS TABLE
# -----------------------------

class Reminder(Base):

    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String)

    reminder_type = Column(String)

    schedule_time = Column(String)

    template_name = Column(String)

    recurring = Column(String)


# -----------------------------
# MESSAGE LOG TABLE
# -----------------------------

class MessageLog(Base):

    __tablename__ = "message_logs"

    id = Column(Integer, primary_key=True, index=True)

    recipient_email = Column(String)

    subject = Column(String)

    status = Column(String)

    timestamp = Column(String)

    error_message = Column(Text)


# -----------------------------
# CAMPAIGN TABLE
# -----------------------------

class Campaign(Base):

    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)

    campaign_name = Column(String)

    template_used = Column(String)

    total_emails = Column(Integer)

    sent_count = Column(Integer)

    failed_count = Column(Integer)