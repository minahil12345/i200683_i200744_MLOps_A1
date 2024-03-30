import requests


# Define the JSON data to send
data = {
    "bill_length_mm": 39.1,
    "bill_depth_mm": 18.7,
    "flipper_length_mm": 181.0,
    "body_mass_g": 3750.0
}

# Send POST request to Flask app
response = requests.post("http://localhost:5000/predict", json=data)

# Print the response
print(response.json())
