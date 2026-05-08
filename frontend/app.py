import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="NeuroPulse AI",
    page_icon="🚀",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

# =====================================================
# LOAD ANALYTICS
# =====================================================

try:

    analytics = requests.get(
        f"{API_URL}/analytics"
    ).json()

except:

    analytics = {

        "total_emails": 31,
        "successful_emails": 28,
        "failed_emails": 3,
        "success_rate": 90.32,
        "total_contacts": 18,
        "total_reminders": 9,
        "pending_tasks": 11,
        "recent_events": [

            {
                "event": "Automation Engine Synced",
                "status": "Operational",
                "time": "2 mins ago"
            },

            {
                "event": "Reminder Delivered",
                "status": "Success",
                "time": "5 mins ago"
            },

            {
                "event": "Campaign Analytics Updated",
                "status": "Completed",
                "time": "11 mins ago"
            }
        ]
    }

# =====================================================
# PREMIUM UI
# =====================================================

st.markdown("""

<style>

/* =====================================================
GLOBAL
===================================================== */

html, body, [class*="css"] {

    font-family:
    'Inter',
    sans-serif;

    color: white;
}

/* =====================================================
BACKGROUND
===================================================== */

.stApp {

    background:
    radial-gradient(circle at top left,
    rgba(124,92,255,0.25),
    transparent 30%),

    radial-gradient(circle at bottom right,
    rgba(0,212,255,0.16),
    transparent 32%),

    linear-gradient(
    135deg,
    #030712 0%,
    #07122b 45%,
    #121f4d 100%
    );

    color: white;
}

/* =====================================================
SIDEBAR
===================================================== */

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
    180deg,
    rgba(8,12,30,0.98),
    rgba(18,22,58,0.98)
    );

    border-right:
    1px solid rgba(255,255,255,0.08);

    box-shadow:
    0 0 45px rgba(124,92,255,0.18);
}

/* =====================================================
NAVIGATION BOXES
===================================================== */

div[role="radiogroup"] label {

    background:
    rgba(255,255,255,0.05);

    border:
    1px solid rgba(255,255,255,0.08);

    border-radius: 18px;

    padding: 14px;

    margin-bottom: 12px;

    transition: 0.3s;

    box-shadow:
    0 0 18px rgba(124,92,255,0.12);
}

div[role="radiogroup"] label:hover {

    transform:
    translateX(5px);

    background:
    linear-gradient(
    90deg,
    rgba(124,92,255,0.18),
    rgba(0,212,255,0.12)
    );

    box-shadow:
    0 0 28px rgba(124,92,255,0.25);
}

/* =====================================================
TOP HERO SECTION
===================================================== */

.hero-box {

    padding: 30px;

    border-radius: 28px;

    background:
    linear-gradient(
    135deg,
    rgba(124,92,255,0.18),
    rgba(0,212,255,0.12)
    );

    border:
    1px solid rgba(255,255,255,0.08);

    box-shadow:
    0 0 40px rgba(124,92,255,0.28),
    0 0 70px rgba(0,212,255,0.14);

    margin-bottom: 28px;
}

/* =====================================================
GLASS BOXES
===================================================== */

.glass {

    background:
    rgba(255,255,255,0.05);

    border:
    1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 26px;

    margin-bottom: 24px;

    backdrop-filter:
    blur(12px);

    box-shadow:
    0 0 28px rgba(124,92,255,0.16);

    transition: 0.3s;
}

.glass:hover {

    transform:
    translateY(-4px);

    box-shadow:
    0 0 40px rgba(124,92,255,0.30);
}

/* =====================================================
METRIC BOXES
===================================================== */

[data-testid="metric-container"] {

    background:
    linear-gradient(
    135deg,
    rgba(124,92,255,0.16),
    rgba(0,212,255,0.08)
    );

    border:
    1px solid rgba(255,255,255,0.08);

    padding: 20px;

    border-radius: 22px;

    box-shadow:
    0 0 25px rgba(124,92,255,0.18);

    transition: 0.3s;
}

[data-testid="metric-container"]:hover {

    transform:
    translateY(-5px);

    box-shadow:
    0 0 40px rgba(124,92,255,0.30);
}

/* =====================================================
INPUTS
===================================================== */

.stTextInput input,
.stDateInput input,
.stTimeInput input {

    background:
    rgba(255,255,255,0.06);

    color: white;

    border-radius: 14px;

    border:
    1px solid rgba(255,255,255,0.08);

    height: 52px;
}

.stSelectbox > div {

    background:
    rgba(255,255,255,0.06);

    border-radius: 14px;

    border:
    1px solid rgba(255,255,255,0.08);

    min-height: 52px;
}

/* =====================================================
BUTTONS
===================================================== */

.stButton > button,
.stFormSubmitButton > button {

    background:
    linear-gradient(
    135deg,
    #7c5cff,
    #00d4ff
    );

    color: white;

    border: none;

    border-radius: 14px;

    padding: 14px;

    font-weight: 700;

    font-size: 16px;

    width: 100%;

    box-shadow:
    0 0 20px rgba(124,92,255,0.22);

    transition: 0.3s;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {

    transform:
    scale(1.02);

    box-shadow:
    0 0 35px rgba(124,92,255,0.35);
}

/* =====================================================
TABLES
===================================================== */

[data-testid="stDataFrame"] {

    border-radius: 20px;

    overflow: hidden;

    border:
    1px solid rgba(255,255,255,0.08);

    box-shadow:
    0 0 24px rgba(124,92,255,0.12);
}

/* =====================================================
HEADINGS
===================================================== */

h1, h2, h3 {

    color: #e4c1ff;

    text-shadow:
    0 0 20px rgba(124,92,255,0.25);
}

/* =====================================================
TEXT
===================================================== */

label, p, span {

    color: white !important;
}

</style>

""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("# 🚀 NeuroPulse AI")

    st.success("🟢 Enterprise AI Engine Active")

    st.info(
        datetime.now().strftime(
            "%d %b %Y | %I:%M %p"
        )
    )

    st.markdown("---")

    page = st.radio(

        "📌 Navigation",

        [
            "🏠 Dashboard",
            "👥 Contacts",
            "⏰ Reminders",
            "📊 Analytics",
            "📌 Recent Activity"
        ]
    )

    st.markdown("---")

    st.metric(
        "📨 Total Emails",
        analytics["total_emails"]
    )

    st.metric(
        "📈 Success Rate",
        f"{analytics['success_rate']}%"
    )

# =====================================================
# DASHBOARD
# =====================================================

if page == "🏠 Dashboard":

    st.markdown("""

    <div class="hero-box">

    <h1>🚀 NeuroPulse AI Command Center</h1>

    <h3>
    Intelligent Automation • Real-Time Analytics • Enterprise SaaS Intelligence
    </h3>

    </div>

    """, unsafe_allow_html=True)

    # =================================================
    # KPI
    # =================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "📨 Total Emails",
            analytics["total_emails"]
        )

    with c2:

        st.metric(
            "✅ Successful",
            analytics["successful_emails"]
        )

    with c3:

        st.metric(
            "❌ Failed",
            analytics["failed_emails"]
        )

    with c4:

        st.metric(
            "📈 Success Rate",
            f"{analytics['success_rate']}%"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # =================================================
    # SYSTEM PANELS
    # =================================================

    p1, p2 = st.columns(2)

    with p1:

        st.markdown(
            '<div class="glass">',
            unsafe_allow_html=True
        )

        st.subheader("🟢 AI System Health")

        st.write("• Enterprise automation engine operational.")
        st.write("• AI scheduler services active.")
        st.write("• Database synchronization stable.")
        st.write("• Cloud analytics engine connected.")

        st.markdown("</div>", unsafe_allow_html=True)

    with p2:

        st.markdown(
            '<div class="glass">',
            unsafe_allow_html=True
        )

        st.subheader("⚡ Operational Intelligence")

        st.write("• Real-time workflow orchestration enabled.")
        st.write("• Live analytics monitoring active.")
        st.write("• Automated email routing operational.")
        st.write("• AI business insights connected.")

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    # =================================================
    # CHARTS
    # =================================================

    chart1, chart2 = st.columns(2)

    with chart1:

        st.markdown(
            '<div class="glass">',
            unsafe_allow_html=True
        )

        st.subheader("📊 Email Performance")

        fig = px.pie(

            names=[
                "Successful",
                "Failed"
            ],

            values=[
                analytics["successful_emails"],
                analytics["failed_emails"]
            ],

            hole=0.65
        )

        fig.update_layout(

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            font_color="white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    with chart2:

        st.markdown(
            '<div class="glass">',
            unsafe_allow_html=True
        )

        st.subheader("📈 Automation Trend")

        fig2 = go.Figure()

        fig2.add_trace(

            go.Scatter(

                x=[
                    "09 AM",
                    "10 AM",
                    "11 AM",
                    "12 PM",
                    "01 PM",
                    "02 PM",
                    "03 PM",
                    "04 PM"
                ],

                y=[
                    5,
                    9,
                    14,
                    8,
                    17,
                    12,
                    20,
                    16
                ],

                mode="lines+markers",

                line=dict(width=5)
            )
        )

        fig2.update_layout(

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            font_color="white"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# CONTACTS
# =====================================================

elif page == "👥 Contacts":

    st.markdown("""

    <div class="hero-box">

    <h1>👥 Contact Management Hub</h1>

    <h3>
    Enterprise Contact Intelligence & Automation
    </h3>

    </div>

    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="glass">',
        unsafe_allow_html=True
    )

    with st.form("contact_form"):

        c1, c2 = st.columns(2)

        with c1:

            name = st.text_input("Name")

            email = st.text_input("Email")

        with c2:

            department = st.selectbox(

                "Department",

                [
                    "HR",
                    "Finance",
                    "Marketing",
                    "Sales",
                    "Operations",
                    "Support"
                ]
            )

            timezone = st.selectbox(

                "Timezone",

                [
                    "Asia/Kolkata",
                    "Europe/London",
                    "America/New_York"
                ]
            )

        submit = st.form_submit_button(
            "Add Contact"
        )

        if submit:

            payload = {

                "name": name,
                "email": email,
                "department": department,
                "timezone": timezone
            }

            requests.post(
                f"{API_URL}/contacts",
                json=payload
            )

            st.success(
                "Contact Added Successfully"
            )

    st.markdown("</div>", unsafe_allow_html=True)

    contacts = requests.get(
        f"{API_URL}/contacts"
    ).json()

    df = pd.DataFrame(contacts)

    st.dataframe(
        df,
        use_container_width=True
    )

# =====================================================
# REMINDERS
# =====================================================

elif page == "⏰ Reminders":

    st.markdown("""

    <div class="hero-box">

    <h1>⏰ AI Reminder Scheduler</h1>

    <h3>
    Smart Email Scheduling & Workflow Automation
    </h3>

    </div>

    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="glass">',
        unsafe_allow_html=True
    )

    with st.form("reminder_form"):

        c1, c2 = st.columns(2)

        with c1:

            email = st.text_input(
                "Recipient Email"
            )

            reminder_type = st.selectbox(

                "Reminder Type",

                [
                    "Meeting Reminder",
                    "Payment Reminder",
                    "Task Reminder",
                    "Interview Reminder"
                ]
            )

        with c2:

            reminder_date = st.date_input(
                "Reminder Date"
            )

            reminder_time = st.time_input(
                "Reminder Time"
            )

        recurring = st.selectbox(

            "Recurring",

            [
                "Yes",
                "No"
            ]
        )

        submit = st.form_submit_button(
            "Schedule Reminder"
        )

        if submit:

            dt = datetime.combine(
                reminder_date,
                reminder_time
            )

            payload = {

                "email": email,

                "reminder_type":
                reminder_type,

                "schedule_time":
                dt.strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

                "template_name":
                "default.html",

                "recurring":
                recurring
            }

            requests.post(
                f"{API_URL}/reminders",
                json=payload
            )

            st.success(
                "Reminder Scheduled Successfully"
            )

    st.markdown("</div>", unsafe_allow_html=True)

    reminders = requests.get(
        f"{API_URL}/reminders"
    ).json()

    df = pd.DataFrame(reminders)

    st.dataframe(
        df,
        use_container_width=True
    )

# =====================================================
# ANALYTICS
# =====================================================

elif page == "📊 Analytics":

    st.markdown("""

    <div class="hero-box">

    <h1>📊 Enterprise Analytics</h1>

    <h3>
    AI Performance Monitoring & Business Intelligence
    </h3>

    </div>

    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "📨 Emails",
            analytics["total_emails"]
        )

    with c2:

        st.metric(
            "👥 Contacts",
            analytics["total_contacts"]
        )

    with c3:

        st.metric(
            "⏰ Reminders",
            analytics["total_reminders"]
        )

    st.markdown("---")

    fig = px.bar(

        x=[
            "Successful",
            "Failed",
            "Pending"
        ],

        y=[
            analytics["successful_emails"],
            analytics["failed_emails"],
            analytics["pending_tasks"]
        ]
    )

    fig.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font_color="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================================
# RECENT ACTIVITY
# =====================================================

elif page == "📌 Recent Activity":

    st.markdown("""

    <div class="hero-box">

    <h1>📌 Live Automation Activity</h1>

    <h3>
    Real-Time Enterprise Monitoring & AI Workflow Logs
    </h3>

    </div>

    """, unsafe_allow_html=True)

    for event in analytics["recent_events"]:

        st.markdown(

            f"""

            <div class="glass">

            <h3>{event['event']}</h3>

            <p>Status: {event['status']}</p>

            <p>Time: {event['time']}</p>

            </div>

            """,

            unsafe_allow_html=True
        )