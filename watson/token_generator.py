import os
import requests

def generate_token():
    # Read the API key from the environment variable
    api_url = "https://iam.cloud.ibm.com/identity/token"
    api_key = os.getenv('API_KEY')

    if not api_key:
        print("Error: API_KEY environment variable not set.")
        exit()

    # Prepare headers and data for the request
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    data = {
        'grant_type': 'urn:ibm:params:oauth:grant-type:apikey',
        'apikey': api_key
    }
    
    try:
        # Make the HTTPS POST request to the API to generate the token
        response = requests.post(api_url, headers=headers, data=data)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Extract the token from the response JSON
            token_data = response.json()
            access_token = token_data.get('access_token')
            return access_token
        else:
            # If the response is not successful, raise an error with the status code
            response.raise_for_status()
    
    except requests.exceptions.RequestException as e:
        # Handle exceptions (e.g., network issues, invalid response)
        print(f"Error occurred: {e}")
        exit()
