import streamlit as st
from database import create_tables, add_part, get_parts

st.set_page_config(page_title="Junkyard Dashboard", layout="wide")

create_tables()

st.title("🏭 Junkyard Dashboard")

st.subheader("➕ Add New Car Part")

with st.form("add_part"):
    car = st.text_input("Car Brand & Model")
    year = st.text_input("Year")
    part = st.text_input("Part Name")
    price = st.text_input("Price (SAR)")
    note = st.text_area("Note")
    image = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    submit = st.form_submit_button("Add Part")

    if submit:
        if car and part and price and image:
            add_part(
                car, year, part, price, note,
                image.read()
            )
            st.success("✅ Saved to database")
        else:
            st.error("❌ Fill all required fields")

st.divider()
st.subheader("📦 Listed Parts")

parts = get_parts()

if not parts:
    st.info("No parts yet")
else:
    for p in parts:
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(p[6], use_container_width=True)

        with col2:
            st.markdown(f"""
            **Part:** {p[3]}  
            **Car:** {p[1]} ({p[2]})  
            **Price:** 💰 {p[4]} SAR  
            **Note:** {p[5]}
            """)

        st.divider()
