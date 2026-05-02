import pickle

model = pickle.load(open("model.pkl", "rb"))
cv = pickle.load(open("encoder.pkl", "rb"))

def predict(branch, skills):
    text = branch + " " + skills
    vec = cv.transform([text])
    return model.predict(vec)[0]

print(predict("CSE", "python machine learning"))
print(predict("IT", "react node mongodb"))
print(predict("ECE", "iot sensors arduino"))