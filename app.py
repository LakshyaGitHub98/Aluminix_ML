import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Correct paths (NEW STRUCTURE)
model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/encoder.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # ✅ Extract skills only (as per training)
        skills = data.get("skills", "").lower().strip()

        if not skills:
            return jsonify({
                "error": "Skills are required",
                "success": False
            }), 400

        print("INPUT →", skills)  # debug

        # ✅ Transform using vectorizer
        vector = vectorizer.transform([skills])

        # ✅ Predict
        prediction = model.predict(vector)[0]

        return jsonify({
            "prediction": prediction,
            "success": True
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({
            "error": str(e),
            "success": False
        }), 500


# ✅ Run server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)