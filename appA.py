import streamlit as st
from supabase import create_client, Client
import os
from dotenv import load_dotenv

# --- Load environment variables ---
load_dotenv()
SUPABASE_URL = "https://xfbefiagysovjxcboeed.supabase.co"
SUPABASE_KEY = "sb_publishable_HZsjY9kXYcDsC2r1YongOQ_O-BAF84E"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- Streamlit Config ---
st.set_page_config(page_title="College Tech Event", page_icon="🎓", layout="centered")

# --- Sidebar Navigation ---
page = st.sidebar.selectbox("Navigate", ["Registration", "Admin"])

# --- Registration Page ---
if page == "Registration":
    st.title("🎓 College Technical Event Registration")

    with st.form("registration_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        department = st.selectbox("Department", ["CSE", "ECE", "IT", "Mechanical", "Civil", "Other"])
        year = st.selectbox("Year", ["1st", "2nd", "3rd", "4th"])
        submit = st.form_submit_button("Register")

        if submit:
            if name and email:
                data = {"name": name, "email": email, "department": department, "year": year}
                supabase.table("participants").insert(data).execute()
                st.success(f"✅ {name} registered successfully!")
            else:
                st.error("Please fill in all required fields.")

# --- Admin Page ---
elif page == "Admin":
    st.title("🔑 Admin Dashboard")

    # Simple password protection
    admin_pass = st.text_input("Enter Admin Password", type="password")
    if admin_pass == "admin123":  # change this to a secure password
        st.success("Access granted ✅")

        participants = supabase.table("participants").select("*").execute()

        if participants.data:
            st.subheader("📋 Registered Participants")
            st.table(participants.data)
        else:
            st.info("No participants registered yet.")
    elif admin_pass:
        st.error("❌ Incorrect password")