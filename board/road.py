from .edge import Edge
from .player import Player


class Road(object):
    def __init__(self, edge, player):
        assert isinstance(edge, Edge)
        self.edge = edge
        assert isinstance(player, Player)
        self.player = player
