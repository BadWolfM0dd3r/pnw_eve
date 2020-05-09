import time
import requests
import json
import redis
from settings import (
    PNW_BASE_URL,
    PNW_API_KEY,
)

class Cron:
    def __init__(self):
        self.api_key = PNW_API_KEY
        self.base_url = PNW_BASE_URL
        self.redis = redis.Redis(host='localhost', port=6379)

    def get_all_nations(self):
        print('Fetching all PNW Nations')

        before = time.monotonic()
        response = requests.get(f'{self.base_url}/nations/?key={self.api_key}').json()

        self.redis.set('nations', json.dumps(response['nations']), ex=3600)

        print(f'Fetched {len(response["nations"])} nations - {int((time.monotonic() - before) * 1000)}ms')

    def get_all_cities(self):
        print('Fetching all PNW Cities')

        before = time.monotonic()
        response = requests.get(f'{self.base_url}/all-cities/?key={self.api_key}')
        result = response.text.replace(',,', ',') # double comma on char 2023114

        self.redis.set('cities', result, ex=3600)

        print(f'Fetched {len(json.loads(result)["all_cities"])} cities - {int((time.monotonic() - before) * 1000)}ms')

if __name__ == '__main__':
    cron = Cron()
    cron.get_all_nations()
    cron.get_all_cities()
