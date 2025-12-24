import joblib
import numpy as np
import pandas as pd

model = joblib.load("model/model.pkl")

# Load the symptom list from Training.csv header (excluding the last column)
TRAINING_CSV = "data/Training.csv"
SYMPTOM_LIST = list(pd.read_csv(TRAINING_CSV, nrows=1).columns)[:-1]

def predict_disease_with_explanation(symptoms):
    # symptoms: list of symptom strings
    # Create one-hot encoded input matching Training.csv columns
    input_vector = [1 if s in symptoms else 0 for s in SYMPTOM_LIST]
    encoded = np.array([input_vector])

    probs = model.predict_proba(encoded)[0]
    classes = model.classes_

    best_idx = np.argmax(probs)
    disease = classes[best_idx]
    confidence = probs[best_idx]

    # Explainability: show which symptoms matched
    contributions = [(SYMPTOM_LIST[i], 1.0) for i, v in enumerate(input_vector) if v == 1]

    return disease, confidence, contributions[:5]
