from apscheduler.schedulers.blocking import BlockingScheduler

from src.scheduler import send_reminders

scheduler = BlockingScheduler()

# -----------------------------------
# RUN EVERY 1 MINUTE
# -----------------------------------

scheduler.add_job(
    send_reminders,
    trigger="interval",
    minutes=1
)

print("\n🚀 Email Automation Worker Started")
print("⏰ Running Every 1 Minute...\n")

scheduler.start()