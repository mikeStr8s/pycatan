from .tile import Tile


class Edge(object):
    verts = set()

    def __init__(self, vert1, vert2):
        assert isinstance(vert1, Vertex)
        assert isinstance(vert2, Vertex)
        self.verts = {vert1, vert2}

    def __eq__(self, other):
        assert isinstance(other, Edge)
        return self.verts == other.verts

    def is_adjacent(self, other):
        assert isinstance(other, Edge)
        if len(self.verts & other.verts) == 1:
            return True
        else:
            return False


class Vertex(object):
    tiles = set()

    def __init__(self, tile1, tile2, tile3):
        assert isinstance(tile1, Tile)
        assert isinstance(tile2, Tile)
        assert isinstance(tile3, Tile)
        self.tiles = {tile1, tile2, tile3}

    def __eq__(self, other):
        assert isinstance(other, Vertex)
        return self.tiles == other.tiles

    def is_adjacent(self, other):
        assert isinstance(other, Vertex)
        if len(self.tiles & other.tiles) == 2:
            return True
        else:
            return False


class Board(object):
    def __init__(self):
        self.tiles = {}
        self.settlements = []
        self.roads = []
        self.vertices = []
        self.edges = []

    def get_tile(self, x, y):
        return self.tiles[Board._pos_to_key(x, y)]

    @staticmethod
    def _pos_to_key(x, y):
        return '{}-{}'.format(x, y)

    def generate_tile_row(self, num_hex, y):
        for x in range(num_hex):
            self.tiles[Board._pos_to_key(x, y)] = Tile()
