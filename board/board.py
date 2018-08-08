from .tile import Tile
from math import pi, cos, sin, sqrt


class Edge(object):
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
    def __init__(self, coordinates):
        self.tiles = []
        assert isinstance(coordinates, list)
        self.coordinates = coordinates

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


class Board(object):
    def __init__(self):
        self.tiles = {}
        self.settlements = []
        self.roads = []
        self.vertices = []
        self.edges = []
        self.side_length = 300
        self.size = 30
        self.tile_width = sqrt(3) * self.size
        self.tile_height = 2 * self.size
        self.horiz_spacing = self.tile_width
        self.vert_spacing = self.tile_height * (3/4)

    def get_tile(self, x, y):
        return self.tiles[Board._pos_to_key(x, y)]

    @staticmethod
    def _pos_to_key(x, y):
        return '{}-{}'.format(x, y)

    def _find_edges(self, tile):
        for v in range(6):
            if v is 5:
                self.edges.append(Edge(tile.vertices[v], tile.vertices[0]))
            else:
                self.edges.append(Edge(tile.vertices[v], tile.vertices[v+1]))

    def generate_tile_row(self, num_tiles, y):
        offset = 0  # Default offset of zero
        if y == 1 or y == 3:  # If the row on the game board requires only a single offset
            offset = 0 - (self.tile_width / 2)
        elif y == 2:  # If the row on the game board requires two offsets
            offset = 0 - self.tile_width

        height = self.vert_spacing * y  # Full vertex vertical spacing

        # All tile center-points for current row
        tile_centers = [[tile * self.horiz_spacing + offset, height] for tile in range(num_tiles)]

        for x, center in enumerate(tile_centers):
            tile = Tile()

            for corner in range(6):
                angle_deg = 60 * corner - 30
                angle_rad = pi / 180 * angle_deg
                x_val = int(round(center[0] + self.size * cos(angle_rad)))
                y_val = int(round(center[1] + self.size * sin(angle_rad)))
                vertex_coordinates = [x_val, y_val]
                vertex = Vertex(vertex_coordinates)

                if self.vertices:  # If there are values in self.vertices
                    all_vertex_coords = [v.coordinates for v in self.vertices]
                    if vertex_coordinates in all_vertex_coords:  # If the vertex already exists
                        for v in self.vertices:
                            if v.coordinates == vertex_coordinates:
                                tile.vertices.append(v)  # Add existing vertex to the tile object
                                v.add_tile(tile)
                                break
                    else:  # If the new vertex does not exist in self.vertices
                        # Add the new vertex to the tile object and self.vertices
                        tile.vertices.append(vertex)
                        self.vertices.append(vertex)
                        vertex.add_tile(tile)
                else:  # If self.vertices is empty
                    # Add new vertex to the tile object and self.vertices
                    tile.vertices.append(vertex)
                    self.vertices.append(vertex)
                    vertex.add_tile(tile)
            tile_id = Board._pos_to_key(x, y)
            tile.tile_id = tile_id
            self.tiles[tile_id] = tile  # Add tile to the tiles coordinate structure
            self._find_edges(tile)
