import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Email Automation Dashboard",
    page_icon="📧",
    layout="wide"
)

# -----------------------------------
# LOAD DATA
# -----------------------------------

contacts_df = pd.read_csv(
    "../backend/data/contacts.csv"
)

reminders_df = pd.read_csv(
    "../backend/data/reminders.csv"
)

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.title("📧 Automation System")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Contacts",
        "Reminders",
        "Analytics"
    ]
)

# -----------------------------------
# DASHBOARD PAGE
# -----------------------------------

if menu == "Dashboard":

    st.title("📧 Email Automation Dashboard")

    st.markdown("---")

    # -------------------------------
    # KPI CARDS
    # -------------------------------

    total_contacts = len(contacts_df)

    total_reminders = len(reminders_df)

    successful_emails = 8

    failed_emails = 2

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "👥 Contacts",
        total_contacts
    )

    col2.metric(
        "⏰ Reminders",
        total_reminders
    )

    col3.metric(
        "✅ Sent",
        successful_emails
    )

    col4.metric(
        "❌ Failed",
        failed_emails
    )

    st.markdown("---")

    # -------------------------------
    # PIE CHART
    # -------------------------------

    chart_data = pd.DataFrame({
        "Status": ["Sent", "Failed"],
        "Count": [successful_emails, failed_emails]
    })

    pie_chart = px.pie(
        chart_data,
        names="Status",
        values="Count",
        title="Email Delivery Status"
    )

    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )

# -----------------------------------
# CONTACTS PAGE
# -----------------------------------

elif menu == "Contacts":

    st.title("👥 Contact Management")

    st.dataframe(
        contacts_df,
        use_container_width=True
    )

# -----------------------------------
# REMINDERS PAGE
# -----------------------------------

elif menu == "Reminders":

    st.title("⏰ Reminder Schedule")

    st.dataframe(
        reminders_df,
        use_container_width=True
    )

# -----------------------------------
# ANALYTICS PAGE
# -----------------------------------

elif menu == "Analytics":

    st.title("📈 Analytics Dashboard")

    department_count = contacts_df[
        "department"
    ].value_counts()

    dept_df = pd.DataFrame({
        "Department": department_count.index,
        "Count": department_count.values
    })

    bar_chart = px.bar(
        dept_df,
        x="Department",
        y="Count",
        title="Department-wise Contacts"
    )

    st.plotly_chart(
        bar_chart,
        use_container_width=True
    )

    recurring_count = reminders_df[
        "recurring"
    ].value_counts()

    recurring_df = pd.DataFrame({
        "Recurring": recurring_count.index,
        "Count": recurring_count.values
    })

    recurring_chart = px.pie(
        recurring_df,
        names="Recurring",
        values="Count",
        title="Recurring vs One-Time Reminders"
    )

    st.plotly_chart(
        recurring_chart,
        use_container_width=True
    )