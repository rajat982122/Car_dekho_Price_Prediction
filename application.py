from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load your exported preprocessor + trained model
preprocessor = pickle.load(open("preprocessor.pkl", "rb"))
model = pickle.load(open("regression.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)

        # Build a single-row DataFrame with EXACT column names your preprocessor expects
        row = pd.DataFrame([{
            "model": data["model"],
            "vehicle_age": float(data["vehicle_age"]),
            "km_driven": float(data["km_driven"]),
            "seller_type": data["seller_type"],
            "fuel_type": data["fuel_type"],
            "transmission_type": data["transmission_type"],
            "mileage": float(data["mileage"]),
            "engine": float(data["engine"]),
            "max_power": float(data["max_power"]),
            "seats": float(data["seats"])
        }])

        X = preprocessor.transform(row)
        y_pred = model.predict(X)[0]

        # round sensibly for price
        return jsonify({"price": round(float(y_pred), 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
