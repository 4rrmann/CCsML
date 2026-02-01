import streamlit as st
import requests

st.set_page_config(page_title="Placement Predictor", page_icon="🎓")

st.title("Placement Prediction System")
st.write("Enter your details to check placement chances")

cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
iq = st.number_input("IQ", min_value=50, max_value=200, step=1)

if st.button("Predict Placement"):
    url = "http://127.0.0.1:8000/predict"
    params = {"cgpa": cgpa, "iq": iq}

    response = requests.post(url, params=params)

    if response.status_code == 200:
        result = response.json()["prediction"]

        if result == "Placed":
            st.success("Congratulations! You are likely to be placed.")
        else:
            st.error("Placement chances are low.")