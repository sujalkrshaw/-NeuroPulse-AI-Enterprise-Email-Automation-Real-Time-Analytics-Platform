import pandas as pd

def load_contacts(path):
    try:
        contacts = pd.read_csv(path)
        print("✅ Contacts Loaded Successfully")
        return contacts

    except Exception as e:
        print(f"❌ Error loading contacts: {e}")
        return None


def load_reminders(path):
    try:
        reminders = pd.read_csv(path)
        print("✅ Reminders Loaded Successfully")
        return reminders

    except Exception as e:
        print(f"❌ Error loading reminders: {e}")
        return None
    

def validate_contacts(df):

    required_columns = [
        "name",
        "email",
        "department",
        "timezone"
    ]

    for column in required_columns:
        if column not in df.columns:
            print(f"❌ Missing column: {column}")
            return False

    print("✅ Contact Data Validated")
    return True


def validate_reminders(df):

    required_columns = [
        "email",
        "reminder_type",
        "schedule_time",
        "template_name",
        "recurring"
    ]

    for column in required_columns:
        if column not in df.columns:
            print(f"❌ Missing column: {column}")
            return False

    print("✅ Reminder Data Validated")
    return True    