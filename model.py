from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
cv = pickle.load(open("encoder.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data["branch"] + " " + data["skills"]

    vec = cv.transform([text])
    prediction = model.predict(vec)[0]

    return jsonify({"career": prediction})

if __name__ == "__main__":
    app.run(debug=True)