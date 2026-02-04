import streamlit as st
import sqlite3
from datetime import datetime

# ---------- DB ----------
conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS deliveries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_type TEXT,
    quantity INTEGER,
    pickup_location TEXT,
    delivery_location TEXT,
    price REAL,
    status TEXT,
    created_at TEXT
)
""")
conn.commit()

# ---------- Helpers ----------
def calculate_price(quantity):
    base_price = 50
    return base_price + (quantity * 20)

# ---------- UI ----------
st.title("🚗 Used Car Equipment Delivery")

menu = st.sidebar.selectbox("Menu", ["Create Delivery", "Track Deliveries", "Admin"])

# ---------- Create ----------
if menu == "Create Delivery":
    st.subheader("Create Delivery Request")

    item_type = st.text_input("Item Type (rims, parts, accessories)")
    quantity = st.number_input("Quantity", min_value=1, step=1)
    pickup = st.text_input("Pickup Location")
    delivery = st.text_input("Delivery Location")

    if st.button("Submit Request"):
        price = calculate_price(quantity)
        c.execute("""
            INSERT INTO deliveries 
            (item_type, quantity, pickup_location, delivery_location, price, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (item_type, quantity, pickup, delivery, price, "Requested", str(datetime.now())))
        conn.commit()

        st.success(f"Request created! Estimated price: {price} SAR")

# ---------- Track ----------
elif menu == "Track Deliveries":
    st.subheader("Your Deliveries")

    rows = c.execute("SELECT * FROM deliveries").fetchall()
    for r in rows:
        st.info(f"""
        ID: {r[0]}
        Item: {r[1]}
        Qty: {r[2]}
        From: {r[3]}
        To: {r[4]}
        Price: {r[5]} SAR
        Status: {r[6]}
        """)

# ---------- Admin ----------
elif menu == "Admin":
    st.subheader("Admin Panel")

    rows = c.execute("SELECT * FROM deliveries").fetchall()
    for r in rows:
        new_status = st.selectbox(
            f"Update status for Order {r[0]}",
            ["Requested", "Picked Up", "In Transit", "Delivered"],
            index=["Requested", "Picked Up", "In Transit", "Delivered"].index(r[6])
        )

        if st.button(f"Update {r[0]}"):
            c.execute("UPDATE deliveries SET status=? WHERE id=?", (new_status, r[0]))
            conn.commit()
            st.success("Status updated")
