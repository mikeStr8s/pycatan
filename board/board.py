from .tile import Tile
from .settlement import Settlement
from .vertex import Vertex
from .edge import Edge
from .player import Player
from math import pi, cos, sin, sqrt


class PlacementException(Exception):
    pass


class Board(object):
    def __init__(self):
        self.tiles = {}
        self.settlements = []
        self.roads = []
        self.vertices = []
        self.edges = []
        self.players = {}

        self.side_length = 500
        self.size = 30
        self.tile_width = sqrt(3) * self.size
        self.tile_height = 2 * self.size
        self.horiz_spacing = self.tile_width
        self.vert_spacing = self.tile_height * (3/4)

        # Generate board tiles
        self.generate_tile_row(3, 0)
        self.generate_tile_row(4, 1)
        self.generate_tile_row(5, 2)
        self.generate_tile_row(4, 3)
        self.generate_tile_row(3, 4)

    def get_tile(self, x, y):
        return self.tiles[Board._pos_to_key(x, y)]

    def create_players(self, count):
        colors = ['red', 'green', 'blue', 'white']
        for x in range(count):
            self.players[x] = Player('Player-{}'.format(x), colors[x])

    def place_settlement(self, vertex, player):
        assert isinstance(vertex, Vertex)
        assert isinstance(player, Player)
        for s in self.settlements:
            if vertex.is_adjacent(s.vertex):
                raise PlacementException('Selected vertex is adjacent to another settlement')
        self.settlements.append(Settlement(vertex, player))

    @staticmethod
    def _pos_to_key(x, y):
        return '{}-{}'.format(x, y)

    def _find_edges(self, tile):
        for v in range(6):
            copied = False
            if v is 5:
                new_edge = Edge(tile.vertices[v], tile.vertices[0])
                for e in self.edges:
                    if e.verts == new_edge.verts:
                        copied = True
                if not copied:
                    self.edges.append(new_edge)
            else:
                new_edge = Edge(tile.vertices[v], tile.vertices[v+1])
                for e in self.edges:
                    if e.verts == new_edge.verts:
                        copied = True
                if not copied:
                    self.edges.append(new_edge)

    def generate_tile_row(self, num_tiles, y):
        x_offset = (self.side_length / 2) - self.horiz_spacing  # Default x_offset of zero
        if y == 1 or y == 3:  # If the row on the game board requires only a single x_offset
            x_offset = x_offset - (self.tile_width / 2)
        elif y == 2:  # If the row on the game board requires two offsets
            x_offset = x_offset - self.tile_width

        y_offset = ((self.side_length / 2) - 2 * self.vert_spacing) + (self.vert_spacing * y)  # Full vertex vertical spacing

        # All tile center-points for current row
        tile_centers = [[tile * self.horiz_spacing + x_offset, y_offset] for tile in range(num_tiles)]

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
