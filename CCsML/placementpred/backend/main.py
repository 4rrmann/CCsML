from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

model = pickle.load(open("placement_model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "Placement Prediction API"}

@app.post("/predict")
def predict(cgpa: float, iq: float):
    features = np.array([[cgpa, iq]])
    prediction = model.predict(features)[0]

    result = "Placed" if prediction == 1 else "Not Placed"
    return {"prediction": result}