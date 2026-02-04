import streamlit as st
from database import create_tables, add_user, get_user

st.set_page_config(page_title="Junkyard Marketplace", layout="centered")
create_tables()

st.title("🚗 Junkyard Marketplace")

if "user" not in st.session_state:
    st.session_state.user = None

menu = st.radio("Choose action", ["Login", "Register"])

if menu == "Register":
    st.subheader("Create account")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["buyer", "junkyard"])

    if st.button("Register"):
        if add_user(email, password, role, name):
            st.success("Account created! You can login now.")
        else:
            st.error("Email already exists")

elif menu == "Login":
    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = get_user(email, password)
        if user:
            st.session_state.user = {
                "id": user[0],
                "role": user[1],
                "name": user[2]
            }
            st.success(f"Welcome {user[2]} 👋")
        else:
            st.error("Invalid email or password")

if st.session_state.user:
    st.divider()
    st.write("Logged in as:", st.session_state.user["role"])