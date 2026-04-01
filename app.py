from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pandas as pd
from model.predict import predict_disease_with_explanation

app = FastAPI()

# Set up the template directory
templates = Jinja2Templates(directory="templates")

# Load all relevant data files
desc_df = pd.read_csv("data/description.csv")
meds_df = pd.read_csv("data/medications.csv")
diet_df = pd.read_csv("data/diets.csv")
prec_df = pd.read_csv("data/precautions_df.csv")
workout_df = pd.read_csv("data/workout_df.csv")

LOW_CONFIDENCE_THRESHOLD = 0.60

EMERGENCY_SYMPTOMS = {
    "chest_pain",
    "severe_bleeding",
    "high_fever",
    "confusion"
}

def check_emergency(symptoms):
    return any(symptom in EMERGENCY_SYMPTOMS for symptom in symptoms)

# Define a Pydantic model for the incoming JSON request
class SymptomRequest(BaseModel):
    symptoms: str

@app.get("/")
def home(request: Request):
    # FastAPI requires passing the 'request' context to templates
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(payload: SymptomRequest):
    # Pydantic automatically parses the JSON, so we just access the attribute
    symptoms = payload.symptoms.split(",")

    disease, confidence, reasons = predict_disease_with_explanation(symptoms)

    consult_doctor = bool(confidence < LOW_CONFIDENCE_THRESHOLD)
    emergency = bool(check_emergency(symptoms))

    # Get description
    desc_row = desc_df[desc_df["Disease"] == disease]
    description = desc_row["Description"].values[0] if not desc_row.empty else ""

    # Get medications
    meds_row = meds_df[meds_df["Disease"] == disease]
    medications = meds_row["Medication"].values[0] if not meds_row.empty else ""

    # Get diet
    diet_row = diet_df[diet_df["Disease"] == disease]
    diet = diet_row["Diet"].values[0] if not diet_row.empty else ""

    # Get precautions (combine all columns except Disease)
    prec_row = prec_df[prec_df["Disease"] == disease]
    if not prec_row.empty:
        precautions = [prec_row[f"Precaution_{i}"].values[0] for i in range(1, 5) if pd.notna(prec_row[f"Precaution_{i}"].values[0])]
    else:
        precautions = []

    # Get workout (all rows for disease, as a list)
    workout_rows = workout_df[workout_df["disease"] == disease]
    workout = workout_rows["workout"].tolist() if not workout_rows.empty else []

    # FastAPI automatically serializes Python dictionaries to JSON responses
    return {
        "disease": disease,
        "confidence": round(confidence * 100, 2),
        "reasons": reasons,
        "consult_doctor": consult_doctor,
        "emergency": emergency,
        "description": description,
        "precaution": precautions,
        "medications": medications,
        "workout": workout,
        "diet": diet
    }

if __name__ == "__main__":
    import uvicorn
    # Replaces app.run(debug=True)
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
