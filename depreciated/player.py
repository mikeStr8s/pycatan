class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.points = 0
        self.longest_road = False
        self.largest_army = False
        self.resources = {
            'brick': 0,
            'wood': 0,
            'wheat': 0,
            'stone': 0,
            'sheep': 0
        }
        self.dev_cards = []
        self.settlements = []
        self.cities = []
