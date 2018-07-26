from .tile import Tile


class Edge(object):
    tiles = set()

    def __init__(self, tile1, tile2, tile3):
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
