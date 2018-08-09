from board.board import Vertex
from .player import Player


class Settlement:
    def __init__(self, vertex, player):
        assert isinstance(vertex, Vertex)
        self.vertex = vertex
        assert isinstance(player, Player)
        self.player = player
        self.level = 1
