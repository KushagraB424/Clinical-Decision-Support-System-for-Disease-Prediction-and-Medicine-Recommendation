import pandas as pd
import joblib
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Load Training.csv (one-hot encoded symptoms, last column is disease label)
df = pd.read_csv("data/Training.csv")

# Features: all columns except the last (prognosis)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# No need for MultiLabelBinarizer, data is already encoded
X_encoded = X.values

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, preds))

# Save model
joblib.dump(model, "model/model.pkl")
