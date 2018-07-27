class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


from math import pi, cos, sin


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


def _hex_corner(self, i):
    angle_deg = 60 * i - 30
    angle_rad = pi / 180 * angle_deg
    return tuple((self.center[0] + self.size * cos(angle_rad), self.center[1] + self.size * sin(angle_rad)))


def _create_hex(self):
    vertices = []
    for x in range(0, 6):
        vertices.append(self._hex_corner(x))
    return vertices

