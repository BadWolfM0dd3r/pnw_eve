import requests
import json
from settings import (
    PNW_API_KEY,
    PNW_BASE_URL,
)

class Nations:
    def __init__(self):
        self.api_key = PNW_API_KEY
        self.base_url = PNW_BASE_URL

    def find_nation(self, nation_id):
        response = requests.get(f'{self.base_url}/nation/id={nation_id}&key={self.api_key}')

        return response.json()

    # def find_nation_in_aa(self, nation_name):
    #     # TODO
