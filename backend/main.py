import pandas as pd

from src.renderer import render_template
from src.mailer import EmailSender

# -----------------------------
# LOAD CONTACTS
# -----------------------------

contacts = pd.read_csv(
    "data/contacts.csv"
)

# -----------------------------
# SELECT FIRST CONTACT
# -----------------------------

user = contacts.iloc[0]

# -----------------------------
# TEMPLATE CONTEXT
# -----------------------------

context = {
    "name": user["name"],
    "reminder_type": "Project Submission",
    "schedule_time": "7 PM Tonight"
}

# -----------------------------
# RENDER HTML
# -----------------------------

html_content = render_template(
    "reminder_template.html",
    context
)

# -----------------------------
# SEND EMAIL
# -----------------------------

mailer = EmailSender()

mailer.send_email(
    recipient_email=user["email"],
    subject="Reminder Notification",
    html_content=html_content
)