class Shared:
    def calculate_military_score(self, soldiers, tanks, planes, ships):
        return (int(soldiers) * 0.0005) + (int(tanks) * 0.05) + (int(planes) * 0.5) + (int(ships) * 2)
