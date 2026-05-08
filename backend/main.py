from src.database import engine
from src.database import Base

from src.models import (
    Contact,
    Reminder,
    MessageLog,
    Campaign
)

# Create database tables
Base.metadata.create_all(bind=engine)

print("✅ Database Created Successfully")
print("✅ Tables Created Successfully")