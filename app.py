import streamlit as st
from database import create_tables

st.set_page_config(page_title="Junkyard Marketplace", layout="centered")

create_tables()

st.title("🚗 Junkyard Marketplace")

st.write("Welcome! Choose your role to continue:")

role = st.radio("I am a:", ["Buyer", "Junkyard"])

if role == "Buyer":
    st.info("Buyer flow coming next")
elif role == "Junkyard":
    st.info("Junkyard flow coming next")
