```python
import requests
from src.api import api_config, api_utils

class APIIntegration:
    def __init__(self):
        self.base_url = api_config.BASE_URL
        self.headers = api_config.HEADERS

    def get_request(self, endpoint):
        try:
            response = requests.get(self.base_url + endpoint, headers=self.headers)
            return api_utils.handle_response(response)
        except Exception as e:
            return api_utils.handle_error(e)

    def post_request(self, endpoint, data):
        try:
            response = requests.post(self.base_url + endpoint, headers=self.headers, data=data)
            return api_utils.handle_response(response)
        except Exception as e:
            return api_utils.handle_error(e)

    def put_request(self, endpoint, data):
        try:
            response = requests.put(self.base_url + endpoint, headers=self.headers, data=data)
            return api_utils.handle_response(response)
        except Exception as e:
            return api_utils.handle_error(e)

    def delete_request(self, endpoint):
        try:
            response = requests.delete(self.base_url + endpoint, headers=self.headers)
            return api_utils.handle_response(response)
        except Exception as e:
            return api_utils.handle_error(e)
```