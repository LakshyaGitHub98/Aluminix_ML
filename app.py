from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model + vectorizer
model = pickle.load(open("model.pkl", "rb"))
cv = pickle.load(open("encoder.pkl", "rb"))

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "AluminiX AI API Running"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        branch = data.get("branch", "")
        skills = data.get("skills", "")

        text = branch + " " + skills
        vec = cv.transform([text])

        prediction = model.predict(vec)[0]

        return jsonify({
            "success": True,
            "career": prediction
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)