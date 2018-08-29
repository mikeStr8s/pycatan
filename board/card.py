class Card(object):
    def __init__(self, card_type):
        self.card_type = card_type
        self.value = None

    def create_resource(self, resource):
        assert self.card_type == 'resource'
        self.value = resource

    def create_development(self, name):
        assert self.card_type == 'development'
        self.value = name
