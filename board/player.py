class Player(object):
    def __init__(self, name, color):
        assert isinstance(name, str)
        self.name = name
        self.color = color
        self.resources = {
            'brick': 0,
            'wood': 0,
            'wheat': 0,
            'stone': 0,
            'sheep': 0
        }
        self.dev_cards = []
        self.settlement_count = 5
        self.city_count = 4
        self.road_count = 15
