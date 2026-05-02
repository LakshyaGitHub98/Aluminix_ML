import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("dataset.csv")

# Combine input features
df["text"] = (
    df["branch"] + " " +
    df["skills"] + " " +
    df["cgpa"].astype(str) + " " +
    df["projects"].astype(str) + " " +
    df["internships"].astype(str) + " " +
    df["communication"].astype(str)
)

X = df["text"]
y = df["career"]

# Vectorizer
cv = CountVectorizer()
X_vec = cv.fit_transform(X)

# Model
model = RandomForestClassifier()
model.fit(X_vec, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(cv, open("encoder.pkl", "wb"))

print("✅ Model trained and saved successfully!")