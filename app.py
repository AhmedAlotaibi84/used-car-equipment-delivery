from flask import Flask, render_template

app = Flask(__name__)

# =====================
# Fake Junkyard Data
# =====================

junkyards = [
    {
        "id": 1,
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
        "id": 2,
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

# =====================
# Routes
# =====================

@app.route("/")
def home():
    return render_template("parts.html", junkyards=junkyards)


if __name__ == "__main__":
    app.run(debug=True)