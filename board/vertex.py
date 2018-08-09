from .tile import Tile


class Vertex(object):
    def __init__(self, coordinates):
        self.tiles = []
        assert isinstance(coordinates, list)
        self.coordinates = coordinates
        self.settlement = None

    def __eq__(self, other):
        assert isinstance(other, Vertex)
        return self.tiles == other.tiles

    def __str__(self):
        return str(self.coordinates)

    def __hash__(self):
        return hash(str(self))

    def is_adjacent(self, other):
        assert isinstance(other, Vertex)
        for idx, tile in enumerate(self.tiles):
            if not tile & other.tiles[idx]:
                return False
        return True

    def add_tile(self, tile):
        assert isinstance(tile, Tile)
        assert len(self.tiles) < 4, len(self.tiles)
        self.tiles.append(tile)
