import streamlit as st
import numpy as np
import pickle

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Car Price Predictor",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown(
    """
    <style>
    /* Background image with dark overlay */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)), 
                    url("https://images.unsplash.com/photo-1503376780353-7e6692767b70?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-position: center;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.75);
        backdrop-filter: blur(8px);
    }

    /* Sidebar inputs */
    [data-testid="stSidebar"] .stSelectbox, 
    [data-testid="stSidebar"] .stNumberInput, 
    [data-testid="stSidebar"] .stSlider {
        background-color: white !important;
        border-radius: 8px;
        padding: 5px;
    }

    /* Sidebar text */
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] span {
        color: white !important;
        font-weight: 600;
    }

    /* Center text styling */
    .main-title {
        font-size: 3rem;
        font-weight: bold;
        color: white;
        text-align: center;
        margin-top: 80px;
    }
    .sub-title {
        font-size: 1.3rem;
        color: white;
        text-align: center;
        margin-bottom: 40px;
    }
    .footer {
        text-align: center;
        color: white;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- MAIN CONTENT ----------
st.markdown('<div class="main-title">🚗 Car Selling Price Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Fill the details in the sidebar and click below to predict the selling price.</div>', unsafe_allow_html=True)

# ---------- SIDEBAR INPUTS ----------
st.sidebar.header("⚙️ Input Car Details")

year = st.sidebar.slider("Model Year", 1990, 2024, 2018)
driven = st.sidebar.slider("Driven Kms", 0, 300000, 30000)
fuel = st.sidebar.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])
seller = st.sidebar.selectbox("Selling Type", ["Dealer", "Individual"])
transmission = st.sidebar.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.sidebar.selectbox("Previous Owners", ["First", "Second", "Third", "More than 3"])

# ---------- PREDICTION BUTTON ----------
if st.sidebar.button("💰 Predict Price"):
    # Dummy prediction (replace with ML model)
    # Example: load model.pkl
    # model = pickle.load(open("model.pkl", "rb"))
    # features = np.array([[year, driven, ...]])
    # prediction = model.predict(features)
    # For now, just make a fake formula
    prediction = max(50000, (2025 - year) * 20000 + (300000 - driven) * 0.5)

    st.success(f"💸 Estimated Selling Price: ₹ {prediction:,.0f}")

# ---------- FOOTER ----------
st.markdown('<div class="footer">Built with ❤️ using Streamlit</div>', unsafe_allow_html=True)
