import streamlit as st
from supabase import create_client, Client

# --- Supabase Config ---
SUPABASE_URL = "https://xfbefiagysovjxcboeed.supabase.co"
SUPABASE_KEY = "SUPABASE_KEY"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- Streamlit UI ---
st.set_page_config(page_title="College Tech Event", page_icon="🎓", layout="centered")

st.title("🎓 College Technical Event Registration")

# Registration Form
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

# Display Participants
st.subheader("📋 Registered Participants")
participants = supabase.table("participants").select("*").execute()

if participants.data:
    st.table(participants.data)
else:
    st.info("No participants registered yet.")