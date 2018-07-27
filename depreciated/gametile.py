from math import pi, cos, sin
from depreciated.utils import Point


class GameTile:
    def __init__(self, tile_id, center, size):
        self.tile_id = tile_id
        self.resource = None
        self.value = None
        self.color = self._get_color(self.resource)
        self.center = center
        self.size = size
        self.vertices = self._create_hex()

    @staticmethod
    def _get_color(resource):
        if resource:
            tile_colors = {
                'brick': 'brown',
                'wood': 'darkgreen',
                'stone': 'grey',
                'wheat': 'yellow',
                'sheep': 'lightgreen',
                'dessert': 'tan'
            }
            return tile_colors[resource]
        return None

    def _hex_corner(self, size, i):
        angle_deg = 60 * i - 30
        angle_rad = pi / 180 * angle_deg
        return Point(self.center.x + size * cos(angle_rad), self.center.y + size * sin(angle_rad))

    def _create_hex(self):
        vertices = []
        for x in range(0, 6):
            vertices.append(self._hex_corner(self.size, x))
        return vertices

    def v_to_arr(self):
        vert = []
        for v in self.vertices:
            vert.append(v.x)
            vert.append(v.y)
        return vert
