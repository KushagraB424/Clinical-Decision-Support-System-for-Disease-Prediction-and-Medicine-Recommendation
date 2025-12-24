Explainable AI-Based Clinical Decision Support System
Overview

This project is an AI-powered clinical decision support system that predicts probable diseases based on user-reported symptoms and provides medicine-related recommendations for educational purposes. The system emphasizes Explainable AI, safety, and ethical design, and is not intended to replace professional medical advice.

Key Features

Disease Prediction using Machine Learning

Predicts likely diseases from a set of symptoms using a Multinomial Naive Bayes classifier.

Explainable AI (XAI)

Displays the top contributing symptoms influencing the prediction.

Shows confidence scores to justify model decisions.

Confidence Thresholding

If prediction confidence is below 60%, the system advises users to consult a medical professional instead of giving recommendations.

Emergency Symptom Detection

Instantly flags critical symptoms such as:

Chest pain

Severe bleeding

High fever with confusion

Displays a prominent emergency warning banner.

Ethical & Safety-First Design

Medicine recommendations are rule-based, not ML-driven.

The system is positioned strictly as a decision support tool, not an automated prescription system.

Full-Stack Web Application

Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript

Technologies Used

Programming Languages: Python, JavaScript

Machine Learning: Scikit-learn (Multinomial Naive Bayes)

Web Framework: Flask

Frontend: HTML, CSS, JavaScript

Data Handling: Pandas, NumPy

Model Persistence: Joblib

Project Structure
medicine_recommendation/
│
├── data/
│   └── dataset.csv
│
├── model/
│   ├── train_model.py
│   ├── predict.py
│   ├── model.pkl
│   └── symptom_encoder.pkl
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── requirements.txt

How It Works

User enters symptoms through the web interface

Symptoms are encoded and passed to the trained ML model

The model predicts the most probable disease and confidence score

Explainable AI module identifies key contributing symptoms

Safety checks:

Low confidence → consult doctor

Emergency symptoms → immediate alert

Disease-specific information (description, precautions, diet, workout, medicines) is displayed

How to Run the Project
1️.Install Dependencies
pip install -r requirements.txt

2️.Train the Model
python model/train_model.py

3️.Start the Application
python app.py

4️4.Open in Browser
http://127.0.0.1:5000

Disclaimer

This project is intended for educational and demonstration purposes only.
It does not provide medical prescriptions and should not be used as a substitute for professional medical consultation.

Future Enhancements

SHAP-based global explainability

PDF health report generation

Multi-language symptom input

Cloud deployment (AWS / Render)

Mobile-responsive UI

Author

Kushagra Gupta
B.Tech – Computer Science (AI & ML)
Manipal Institute of Technology, Manipal
