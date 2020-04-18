import requests
import json
from core.nations import Nations
from core.shared import Shared
from settings import (
    PNW_API_KEY,
    PNW_BASE_URL,
    PNW_ALLIANCE_ID,
)

class Wars:
    def __init__(self):
        self.api_key = PNW_API_KEY
        self.base_url = PNW_BASE_URL
        self.alliance_id = PNW_ALLIANCE_ID

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

    def raid_targets(self, nation_info, alliance_id):
        targets = []

        min_score = f'{float(nation_info["score"]) * 0.75:.2f}'
        max_score = f'{float(nation_info["score"]) * 1.75:.2f}'

        response = requests.get(f'{self.base_url}/nations/?key={self.api_key}&min_score={min_score}\
            &max_score={max_score}&alliance_id={alliance_id}&vm=false').json()

        target_nations = (i for i in response['nations'] if i['color'] != 'beige' and i['war_policy'] != 'Moneybags' and
            i['defensivewars'] < 3 and i['minutessinceactive'] > 10080)

        for target_nation in target_nations:
            target_nation_info = Nations().find_nation(target_nation['nationid'])
            target_nation['gdp'] = target_nation_info['gdp']
            target_nation['soldiers'] = target_nation_info['soldiers']
            target_nation['tanks'] = target_nation_info['tanks']
            target_nation['aircraft'] = target_nation_info['aircraft']
            target_nation['ships'] = target_nation_info['ships']

        # Sort via GDP
        # nations = sorted(nations, key=lambda i: i['gdp'], reverse=False)

        return target_nations

    def counter_targets(self, aggresor_nation):
        ally_nation = []
        agg_defend_min = float(aggresor_nation['score']) / 1.75
        agg_defend_max = float(aggresor_nation['score']) / 0.75

        response = requests.get(f'{self.base_url}/alliance-members/?\
            allianceid={self.alliance_id}&key={self.api_key}').json()

        for nation in response['nations']:
            nation['military_score'] = Shared().calculate_military_score(
                soldiers=nation['soldiers'],
                tanks=nation['tanks'],
                planes=nation['aircraft'],
                ships=nation['ships']
            )

            ally_nation.append(nation)

        ally_nations = [i for i in ally_nation if i['color'] != 'beige'
            and i['vacmode'] == '0'
            and i['offensivewars'] < 5
            # and i['minutessinceactive'] < 4320
            and i['cities'] >= aggresor_nation['cities']
            and i['military_score'] >= aggresor_nation['military_score']
            and float(i['score']) >= agg_defend_min and float(i['score']) <= agg_defend_max]

        sorted_nations = sorted(ally_nations, key=lambda i: (i['cities'], i['military_score']), reverse=True)

        return sorted_nations[:6]
