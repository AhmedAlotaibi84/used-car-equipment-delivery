import streamlit as st
from database import create_tables, add_part, get_parts
from PIL import Image
import io

st.set_page_config(page_title="Junkyard Panel", layout="wide")

create_tables()

st.title("🛠️ Junkyard Dashboard")

st.header("➕ Add New Part")

with st.form("add_part_form"):
    car = st.text_input("Car Make & Model")
    year = st.text_input("Year")
    part = st.text_input("Part Name")
    price = st.text_input("Price")
    note = st.text_area("Note")
    image_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    submitted = st.form_submit_button("Add Part")

    if submitted:
        if image_file:
            image_bytes = image_file.read()
            add_part(car, year, part, price, note, image_bytes)
            st.success("✅ Part added successfully")
        else:
            st.error("❌ Please upload an image")

st.divider()

st.header("📦 Available Parts")

parts = get_parts()

cols = st.columns(3)

for index, p in enumerate(parts):
    with cols[index % 3]:
        st.subheader(f"{p[1]} ({p[2]})")
        st.write(f"**Part:** {p[3]}")
        st.write(f"💰 {p[4]}")
        st.write(p[5])

        if p[6]:
            img = Image.open(io.BytesIO(p[6]))
            st.image(img, use_container_width=True)
