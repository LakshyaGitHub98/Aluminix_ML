import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("data/dataset.csv")

# Clean data
df = df.dropna()

# 🔥 Use only skills
df["skills"] = df["skills"].str.lower()

X = df["skills"]
y = df["career"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Vectorizer
vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2)
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = LogisticRegression(
    max_iter=1000,
    class_weight='balanced'
)

model.fit(X_train_vec, y_train)

# Evaluate
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy:.2f}")

# 🔥 SAVE MODEL (YAHI DAALNA THA)
pickle.dump(model, open("models/model.pkl", "wb"))
pickle.dump(vectorizer, open("models/encoder.pkl", "wb"))

print("\nClass Distribution:\n", df["career"].value_counts())
print("\n✅ Model trained & saved successfully!")