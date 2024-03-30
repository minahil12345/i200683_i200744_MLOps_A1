import requests
import json

# Define the JSON data to send
data = {
    "bill_length_mm": 39.1,
    "bill_depth_mm": 18.7,
    "flipper_length_mm": 181.0,
    "body_mass_g": 3750.0
}

# Send POST request to Flask app
response = requests.post("http://localhost:5000/predict", json=data)

# Check if response is successful
if response.status_code == 200:
    try:
        # Try to parse JSON response
        json_response = response.json()
        print("Predicted species:", json_response['predicted_species'])
    except json.JSONDecodeError:
        # If JSON decoding fails, print raw response
        print("Raw response:", response.text)
else:
    # Print error message if request was unsuccessful
    print("Error:", response.text)
