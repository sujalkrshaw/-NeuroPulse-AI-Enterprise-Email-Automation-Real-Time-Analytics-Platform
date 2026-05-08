import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from src.config import (
    SMTP_HOST,
    SMTP_PORT,
    SMTP_USER,
    SMTP_PASS,
    DRY_RUN
)

from src.logger import (
    sent_logger,
    failed_logger
)

from src.database import SessionLocal

from src.models import EmailEvent


class EmailSender:

    def __init__(self):

        self.host = SMTP_HOST
        self.port = SMTP_PORT

        self.user = SMTP_USER
        self.password = SMTP_PASS

    # -----------------------------------
    # STORE EMAIL EVENT
    # -----------------------------------

    def store_event(
        self,
        recipient_email,
        subject,
        status,
        error_message=None
    ):

        db = SessionLocal()

        event = EmailEvent(

            recipient_email=recipient_email,

            subject=subject,

            status=status,

            error_message=error_message
        )

        db.add(event)

        db.commit()

        db.close()

    # -----------------------------------
    # SEND EMAIL
    # -----------------------------------

    def send_email(
        self,
        recipient_email,
        subject,
        html_content
    ):

        # -----------------------------------
        # DRY RUN MODE
        # -----------------------------------

        if DRY_RUN:

            print("\n============================")
            print("📧 DRY RUN MODE ENABLED")
            print("============================")

            print(f"To: {recipient_email}")
            print(f"Subject: {subject}")

            print("\nHTML Preview:\n")
            print(html_content[:500])

            sent_logger.info(
                f"DRY RUN SUCCESS -> {recipient_email}"
            )

            # STORE EVENT

            self.store_event(
                recipient_email,
                subject,
                "SUCCESS"
            )

            return True

        # -----------------------------------
        # REAL SMTP MODE
        # -----------------------------------

        try:

            message = MIMEMultipart()

            message["From"] = self.user

            message["To"] = recipient_email

            message["Subject"] = subject

            message.attach(
                MIMEText(html_content, "html")
            )

            server = smtplib.SMTP_SSL(
                self.host,
                self.port
            )

            server.login(
                self.user,
                self.password
            )

            server.sendmail(
                self.user,
                recipient_email,
                message.as_string()
            )

            server.quit()

            print(f"✅ Email Sent -> {recipient_email}")

            sent_logger.info(
                f"SENT -> {recipient_email}"
            )

            # STORE SUCCESS EVENT

            self.store_event(
                recipient_email,
                subject,
                "SUCCESS"
            )

            return True

        except Exception as e:

            print(f"❌ Failed -> {recipient_email}")

            print(e)

            failed_logger.error(
                f"FAILED -> {recipient_email} -> {e}"
            )

            # STORE FAILED EVENT

            self.store_event(
                recipient_email,
                subject,
                "FAILED",
                str(e)
            )

            return False