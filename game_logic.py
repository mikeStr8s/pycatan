from board.board import Board, Vertex
from board.tile import Tile

from math import pi, cos, sin, sqrt

size = 30
height = 300
width = 300
vertex_id = 1
hex_width = sqrt(3) * size
hex_height = 2 * size
horiz_spacing = hex_width
vert_spacing = hex_height * (3/4)


def main():
    b = Board()
    t = create_tile(b, [width/2, height/2])
    t2 = create_tile(b, [width/2 + horiz_spacing, height/2])
    print('Done')


def create_tile(board, center):
    tile = Tile()
    for x in range(6):
        v = create_tile_vertex(x, board, center)
        tile.vertices.append(v)

    for idx, v in enumerate(tile.vertices):
        if idx == 5:
            v.add_neighbor(tile.vertices[0])
            v.add_neighbor(tile.vertices[idx - 1])
        elif idx == 0:
            v.add_neighbor(tile.vertices[idx + 1])
            v.add_neighbor(tile.vertices[5])
        else:
            v.add_neighbor(tile.vertices[idx + 1])
            v.add_neighbor(tile.vertices[idx - 1])

    return tile


def create_tile_vertex(i, board, center):
    global vertex_id
    angle_deg = 60 * i - 30
    angle_rad = pi / 180 * angle_deg
    coords = [center[0] + size * cos(angle_rad), center[1] + size * sin(angle_rad)]
    v = Vertex(coords)

    for vertex in board.vertices:
        if v.coordinates == vertex.coordinates:
            return vertex

    v.id = vertex_id
    vertex_id += 1
    board.vertices.append(v)
    return v


if __name__ == '__main__':
    main()
