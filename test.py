import pickle

model = pickle.load(open("models/model.pkl", "rb"))
cv = pickle.load(open("models/encoder.pkl", "rb"))

def predict(skills):
    # same preprocessing as training
    text = skills.lower().strip()
    vec = cv.transform([text])
    return model.predict(vec)[0]

# 🔥 TEST CASES
print("Test 1:", predict("python machine learning ai data analysis"))
print("Test 2:", predict("html css javascript react"))
print("Test 3:", predict("node js express mongodb api"))
print("Test 4:", predict("iot sensors arduino embedded"))