from flask import Flask, jsonify, request
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model
model = joblib.load('Model/logistic_regression_model.joblib')

# Initialize the scaler (make sure to use the same scaler used during training)
scaler = StandardScaler()

# Endpoint for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data sent in the request
    data = request.json
    
    # Convert JSON data to DataFrame
    new_data = pd.DataFrame(data, index=[0])
    
    # Scale the new data using the same scaler used during training
    new_data_scaled = scaler.transform(new_data)
    
    # Make predictions
    predictions = model.predict(new_data_scaled)
    
    # Convert predictions to human-readable labels
    species_mapping = {0: 'Adelie', 1: 'Chinstrap', 2: 'Gentoo'}
    predicted_species = [species_mapping[p] for p in predictions]
    
    # Return predictions as JSON response
    return jsonify({'predicted_species': predicted_species})

if __name__ == '__main__':
    app.run(debug=True)
