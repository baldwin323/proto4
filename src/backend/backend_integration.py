```python
import requests
from src.api import api_config
from src.api import api_utils

class BackendIntegration:
    def __init__(self):
        self.backend_url = api_config.BACKEND_URL
        self.headers = api_config.HEADERS

    def get_data(self, endpoint):
        response = requests.get(self.backend_url + endpoint, headers=self.headers)
        return api_utils.handle_response(response)

    def post_data(self, endpoint, data):
        response = requests.post(self.backend_url + endpoint, headers=self.headers, data=data)
        return api_utils.handle_response(response)

    def put_data(self, endpoint, data):
        response = requests.put(self.backend_url + endpoint, headers=self.headers, data=data)
        return api_utils.handle_response(response)

    def delete_data(self, endpoint):
        response = requests.delete(self.backend_url + endpoint, headers=self.headers)
        return api_utils.handle_response(response)
```