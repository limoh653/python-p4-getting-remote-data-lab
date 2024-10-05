import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        pass
        """Fetches the response body from the URL as a byte string."""
        response = requests.get(self.url)
        response.raise_for_status()  # This will raise an error for HTTP codes 
        return response.content  # Returns the raw byte response

    def load_json(self):
        pass
        """Loads and returns the JSON response as a Python object."""
        response_body = self.get_response_body()  # Call the method to get the response body
        return json.loads(response_body)  # Convert the byte response to a Python dictionary/list
