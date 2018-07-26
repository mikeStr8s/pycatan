from .tile import Tile


class Edge(object):
    tiles = set()

    def __init__(self, tile1, tile2):
        assert isinstance(tile1, Tile)
        assert isinstance(tile2, Tile)
        self.tiles = {tile1, tile2}


class Vert(object):
    tiles = set()

    def __init__(self, tile1, tile2, tile3):
        assert isinstance(tile1, Tile)
        assert isinstance(tile2, Tile)
        assert isinstance(tile3, Tile)
        self.tiles = {tile1, tile2, tile3}


class Board(object):
    def __init__(self):
        self.tiles = {}
        self.settlements = []
        self.roads = []
        self.vertices = []
        self.edges = []

    def get_tile(self, x, y):
        return self.tiles['{}-{}'.format(x, y)]
