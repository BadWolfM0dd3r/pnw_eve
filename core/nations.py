import requests
import json
from core.shared import Shared
from settings import (
    PNW_API_KEY,
    PNW_BASE_URL,
)

class Nations:
    def __init__(self):
        self.api_key = PNW_API_KEY
        self.base_url = PNW_BASE_URL

    def find_nation(self, nation_id):
        response = requests.get(f'{self.base_url}/nation/id={nation_id}&key={self.api_key}').json()

        response['military_score'] = Shared().calculate_military_score(
            soldiers=response['soldiers'],
            tanks=response['tanks'],
            planes=response['aircraft'],
            ships=response['ships']
        )

        return response

    # def find_nation_in_aa(self, nation_name):
    #     # TODO
