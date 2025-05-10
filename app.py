from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import tensorflow as tf
from joblib import load

app = Flask(__name__)

# Load the trained model and preprocessor
def load_assets():
    try:
        model = tf.keras.models.load_model('bmi_model.h5')  # Make sure the model is in your project folder
        preprocessor = load('bmi_preprocessor.joblib')  # Make sure the preprocessor is in your project folder
        return model, preprocessor
    except Exception as e:
        return str(e), None

# Define a route to handle the BMI prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json()

        age = data.get('Age')
        gender = data.get('Gender')
        height = data.get('Height')
        weight = data.get('Weight')

        if not all([age, gender, height, weight]):
            return jsonify({"error": "Missing data, please provide age, gender, height, and weight"}), 400

        # Create input dictionary to match the trained model format
        user_data = {
            'Age': age,
            'Gender': gender,
            'Height': height,
            'Weight': weight
        }

        # Load model and preprocessor
        model, preprocessor = load_assets()

        if model is None:
            return jsonify({"error": f"Error loading assets: {preprocessor}"}), 500

        # Create input DataFrame
        input_df = pd.DataFrame([user_data])

        # Preprocess input and predict
        processed_input = preprocessor.transform(input_df)
        predictions = model.predict(processed_input, verbose=0)
        probabilities = tf.nn.softmax(predictions).numpy()[0]

        categories = ['Underweight', 'Normal', 'Overweight', 'Obese']
        predicted_index = np.argmax(probabilities)
        predicted_category = categories[predicted_index]
        confidence = probabilities[predicted_index]

        result = {
            "Predicted BMI Category": predicted_category,
            "Prediction Confidence": f"{confidence:.2%}",
            "Prediction Probabilities": {cat: f"{prob:.2%}" for cat, prob in zip(categories, probabilities)}
        }

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
