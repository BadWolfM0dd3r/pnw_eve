import json
import os

class WarChest:
    def __init__(self):
        self.chest_json = os.path.abspath('warchest.json')

    def find_warchest(self, city_count):
        f = open(self.chest_json)

        chest = json.load(f)

        f.close()

        return chest[city_count]
