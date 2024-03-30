import unittest
import json
from app import app

class TestFlaskApp(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_predict_endpoint_with_valid_data(self):
        # Sample valid data to send to the /predict endpoint
        valid_data = {
            'bill_length_mm': 39.5,
            'bill_depth_mm': 18.4,
            'flipper_length_mm': 181.0,
            'body_mass_g': 3750.0
        }

        # Send a POST request to the /predict endpoint with valid data
        response = self.app.post('/predict', json=valid_data)
        
        # Check if the status code is 200
        self.assertEqual(response.status_code, 200)
        
        # Decode the JSON response
        response_data = json.loads(response.data)
        
        # Check if the predicted_species key exists in the response
        self.assertIn('predicted_species', response_data)
        
        # Check if the predicted_species value is one of the valid species
        valid_species = ['Adelie', 'Chinstrap', 'Gentoo']
        self.assertIn(response_data['predicted_species'], valid_species)

    def test_predict_endpoint_with_invalid_data(self):
        # Sample invalid data (missing a required field) to send to the /predict endpoint
        invalid_data = {
            'bill_length_mm': 39.5,
            'bill_depth_mm': 18.4,
            'flipper_length_mm': 181.0,
            # Missing 'body_mass_g'
        }

        # Send a POST request to the /predict endpoint with invalid data
        response = self.app.post('/predict', json=invalid_data)
        
        # Check if the status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)
        
        # Decode the JSON response
        response_data = json.loads(response.data)
        
        # Check if the error message is as expected
        self.assertEqual(response_data['message'], 'Missing data: body_mass_g')

if __name__ == '__main__':
    unittest.main()
