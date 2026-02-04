import streamlit as st

st.set_page_config(page_title="Junkyard Marketplace", layout="wide")

st.title("🚗 Junkyard Marketplace")

st.subheader("Available Car Parts")

junkyards = [
    {
        "name": "Riyadh Junkyard",
        "city": "Riyadh",
        "parts": [
            {
                "car": "Toyota Camry",
                "year": "2018",
                "part": "Front Bumper",
                "price": "450 SAR",
                "note": "Original, good condition",
                "image": "https://images.unsplash.com/photo-1542362567-b07e54358753"
            },
            {
                "car": "Toyota Camry",
                "year": "2019",
                "part": "Headlight",
                "price": "300 SAR",
                "note": "Left side",
                "image": "https://images.unsplash.com/photo-1605559424843-9c6dc11f98e3"
            }
        ]
    },
    {
        "name": "Jeddah Auto Parts",
        "city": "Jeddah",
        "parts": [
            {
                "car": "Ford Explorer",
                "year": "2017",
                "part": "Side Mirror",
                "price": "250 SAR",
                "note": "Electric mirror",
                "image": "https://images.unsplash.com/photo-1553440569-bcc63803a83d"
            }
        ]
    }
]

for yard in junkyards:
    st.markdown(f"## 🏭 {yard['name']} — {yard['city']}")

    for part in yard["parts"]:
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(part["image"], use_container_width=True)

        with col2:
            st.markdown(f"""
            **Part:** {part['part']}  
            **Car:** {part['car']} ({part['year']})  
            **Price:** 💰 {part['price']}  
            **Note:** {part['note']}
            """)

        st.divider()