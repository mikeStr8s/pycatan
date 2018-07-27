from .tile import Tile


class Vertex(object):
    def __init__(self, coordinates):
        self._tiles = set()
        self.has_settlement = False
        self._neighbors = set()
        self.coordinates = coordinates
        self.id = None

    def add_neighbor(self, vert):
        assert len(self._neighbors) < 4
        assert isinstance(vert, Vertex)
        self._neighbors.add(vert)

    def add_tile(self, tile):
        assert len(self._tiles) < 4
        assert isinstance(tile, Tile)
        self._tiles.add(tile)

    def is_adjacent(self, other):
        assert isinstance(other, Edge)
        if len(self.verts & other.verts) == 1:
            return True
        else:
            return False


class Edge(object):
    verts = set()

    def __init__(self, vert1, vert2):
        assert isinstance(vert1, Vertex)
        assert isinstance(vert2, Vertex)
        self.verts = {vert1, vert2}

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
