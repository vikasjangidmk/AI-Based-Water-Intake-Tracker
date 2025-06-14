import streamlit as st
import pandas as pd
from datetime import datetime
from src.agent import WaterIntakeAgent
from src.database import log_intake, get_intake_history

# Track whether user has started tracking
if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False

# ------------------------
# 💡 Welcome Section
# ------------------------
if not st.session_state.tracker_started:
    st.title("💧 Welcome to AI Water Tracker")
    st.markdown("""
        Track your daily hydration with the help of an AI assistant.  
        Log your intake, get smart feedback, and stay healthy effortlessly! 🧠💦
    """)

    if st.button("🚀 Start Tracking"):
        st.session_state.tracker_started = True
        st.rerun()

# ------------------------
# 🚰 Tracker Dashboard
# ------------------------
else:
    st.title("💧 AI Water Tracker Dashboard")

    # Sidebar: Intake Input
    st.sidebar.header("Log Your Water Intake")
    user_id = st.sidebar.text_input("User ID", value="user_123")
    intake_ml = st.sidebar.number_input("Water Intake (ml)", min_value=0, step=100)

    if st.sidebar.button("Submit"):
        if user_id and intake_ml:
            log_intake(user_id, intake_ml)
            st.success(f"✅ Logged {intake_ml}ml for {user_id}")

            agent = WaterIntakeAgent()
            feedback = agent.analyze_intake(intake_ml)
            st.info(f"🤖 AI Feedback: {feedback}")

    # Divider
    st.markdown("---")

    # 📊 History Section
    st.header("📈 Water Intake History")

    if user_id:
        history = get_intake_history(user_id)
        if history:
            dates = [datetime.strptime(row[1], "%Y-%m-%d") for row in history]
            values = [row[0] for row in history]

            df = pd.DataFrame({
                "Date": dates,
                "Water Intake (ml)": values
            })

            st.dataframe(df)
            st.line_chart(df, x="Date", y="Water Intake (ml)")
        else:
            st.warning("⚠️ No water intake data found. Please log your intake first.")
