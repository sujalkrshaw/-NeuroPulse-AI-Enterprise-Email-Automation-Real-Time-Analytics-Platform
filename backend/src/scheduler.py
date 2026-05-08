import pandas as pd

from apscheduler.schedulers.blocking import BlockingScheduler

from src.renderer import render_template
from src.mailer import EmailSender

# --------------------------------
# LOAD DATA
# --------------------------------

contacts_df = pd.read_csv(
    "data/contacts.csv"
)

reminders_df = pd.read_csv(
    "data/reminders.csv"
)

# --------------------------------
# MAILER INSTANCE
# --------------------------------

mailer = EmailSender()

# --------------------------------
# SEND REMINDER FUNCTION
# --------------------------------

def send_reminders():

    print("\n===================================")
    print("⏰ Scheduler Running...")
    print("===================================\n")

    for _, reminder in reminders_df.iterrows():

        email = reminder["email"]

        user = contacts_df[
            contacts_df["email"] == email
        ]

        if user.empty:
            print(f"❌ User Not Found -> {email}")
            continue

        user = user.iloc[0]

        # -------------------------
        # TEMPLATE CONTEXT
        # -------------------------

        context = {
            "name": user["name"],
            "reminder_type": reminder["reminder_type"],
            "schedule_time": reminder["schedule_time"]
        }

        # -------------------------
        # RENDER HTML
        # -------------------------

        html_content = render_template(
            reminder["template_name"],
            context
        )

        # -------------------------
        # SEND EMAIL
        # -------------------------

        mailer.send_email(
            recipient_email=email,
            subject=reminder["reminder_type"],
            html_content=html_content
        )

    print("\n✅ Reminder Cycle Completed\n")