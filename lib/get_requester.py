import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Fetch the response body from the URL
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
        return None

    def load_json(self):
        # Parse the response body into JSON
        response_body = self.get_response_body()
        if response_body:
            return json.loads(response_body)
        return None
