from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "Welcome to the House Price Prediction API!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Extract features from JSON
        sqft = data.get("sqft")
        bedrooms = data.get("bedrooms")
        bathrooms = data.get("bathrooms")

        # Ensure all values are provided
        if sqft is None or bedrooms is None or bathrooms is None:
            return jsonify({"error": "Missing one or more input values"}), 400

        # Convert input into NumPy array
        features = np.array([[sqft, bedrooms, bathrooms]])

        # Make prediction
        prediction = model.predict(features)[0]

        # Return result
        return jsonify({"predicted_price": round(prediction, 2)})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
