#  Explainable AI-Based Clinical Decision Support System

## Overview
This project is an AI-powered **clinical decision support system** that predicts probable diseases based on user-reported symptoms and provides medicine-related recommendations for educational purposes. The system emphasizes **Explainable AI, safety, and ethical design**, and is **not intended to replace professional medical advice**.

---

## Live Demo
https://clinical-decision-support-system-for.onrender.com

## Key Features

### Disease Prediction using Machine Learning
- Predicts likely diseases from a set of symptoms using a **Multinomial Naive Bayes** classifier.

### Explainable AI (XAI)
- Displays the **top contributing symptoms** influencing the prediction.
- Shows **confidence scores** to justify model decisions.

### Confidence Thresholding
- If prediction confidence is below **60%**, the system advises users to **consult a medical professional** instead of giving recommendations.

### Emergency Symptom Detection
- Instantly flags critical symptoms such as:
  - Chest pain  
  - Severe bleeding  
  - High fever with confusion  
- Displays a prominent **emergency warning banner**.

### Ethical & Safety-First Design
- Medicine recommendations are **rule-based**, not ML-driven.
- The system is positioned strictly as a **decision support tool**, not an automated prescription system.

### Full-Stack Web Application
- **Backend:** Flask (Python)  
- **Frontend:** HTML, CSS, JavaScript  

---

## Technologies Used

- **Programming Languages:** Python, JavaScript  
- **Machine Learning:** Scikit-learn (Multinomial Naive Bayes)  
- **Web Framework:** Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Data Handling:** Pandas, NumPy  
- **Model Persistence:** Joblib  

---

## How It Works
1. User enters symptoms through the web interface.
2. Symptoms are encoded and passed to the trained machine learning model.
3. The model predicts the most probable disease along with a confidence score.
4. The Explainable AI module identifies the top contributing symptoms influencing the prediction.
5. Safety checks are applied:
   - Low confidence prediction → user is advised to consult a medical professional.
   - Emergency symptoms detected → immediate warning alert is displayed.
6. Disease-specific information such as description, precautions, diet, workout, and medicines is presented to the user.

---

## How to Run the Project

### Step 1: Install Dependencies
pip install -r requirements.txt

### Step 2: Train the Model
python model/train_model.py

### Step 3: Start the Application
python app.py

### Step 4: Open in Browser
http://127.0.0.1:5000

## Disclaimer

This project is intended for educational and demonstration purposes only.
It does not provide medical prescriptions and should not be used as a substitute for professional medical consultation.

## Author

Kushagra Gupta
B.Tech – Computer Science (AI & ML)
Manipal Institute of Technology, Manipal
