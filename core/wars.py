import requests
import json
from core.nations import Nations
from settings import (
    PNW_API_KEY,
    PNW_BASE_URL,
)

class Wars:
    def __init__(self):
        self.api_key = PNW_API_KEY
        self.base_url = PNW_BASE_URL

    def show_offensive_wars(self, war_ids):
        offensive_wars = []

        for war_id in war_ids:
            response = requests.get(f'{self.base_url}/war/{war_id}&key={self.api_key}').json()
            result = response['war'][0]

            defender_nation = Nations().find_nation(result['defender_id'])

            if result['war_type'] == 'ord':
                war_type = 'Ordinary'
            elif result['war_type'] == 'att':
                war_type = 'Attrition'
            else:
                war_type = 'Raid'

            war_link = f'https://politicsandwar.com/nation/war/timeline/war={war_id}'

            offensive_wars.append(
                f'[{war_type} - {defender_nation["name"]} ({result["defender_alliance_name"]})]({war_link})'
            )

        return offensive_wars

    def show_defensive_wars(self, war_ids):
        defensive_wars = []

        for war_id in war_ids:
            response = requests.get(f'{self.base_url}/war/{war_id}&key={self.api_key}').json()
            result = response['war'][0]

            aggresor_nation = Nations().find_nation(result['aggressor_id'])

            if result['war_type'] == 'ord':
                war_type = 'Ordinary'
            elif result['war_type'] == 'att':
                war_type = 'Attrition'
            else:
                war_type = 'Raid'

            war_link = f'https://politicsandwar.com/nation/war/timeline/war={war_id}'

            defensive_wars.append(
                f'[{war_type} - {aggresor_nation["name"]} ({result["aggressor_alliance_name"]})]({war_link})'
            )

        return defensive_wars
