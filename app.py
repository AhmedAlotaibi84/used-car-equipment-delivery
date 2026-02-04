import streamlit as st

st.set_page_config(page_title="Junkyard Dashboard", layout="wide")

# storage (temporary)
if "parts" not in st.session_state:
    st.session_state.parts = []

st.title("🏭 Junkyard Dashboard")

st.subheader("➕ Add New Car Part")

with st.form("add_part_form"):
    car = st.text_input("Car Brand & Model")
    year = st.text_input("Year")
    part_name = st.text_input("Part Name")
    price = st.text_input("Price (SAR)")
    note = st.text_area("Note")
    image = st.file_uploader("Upload Part Image", type=["jpg", "png", "jpeg"])

    submitted = st.form_submit_button("Add Part")

    if submitted:
        if car and part_name and price and image:
            st.session_state.parts.append({
                "car": car,
                "year": year,
                "part": part_name,
                "price": price,
                "note": note,
                "image": image
            })
            st.success("✅ Part added successfully!")
        else:
            st.error("❌ Please fill all required fields")

st.divider()

st.subheader("📦 Your Listed Parts")

if not st.session_state.parts:
    st.info("No parts added yet.")
else:
    for part in st.session_state.parts:
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(part["image"], use_container_width=True)

        with col2:
            st.markdown(f"""
            **Part:** {part['part']}  
            **Car:** {part['car']} ({part['year']})  
            **Price:** 💰 {part['price']} SAR  
            **Note:** {part['note']}
            """)

        st.divider()