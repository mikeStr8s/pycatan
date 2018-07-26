from tkinter import *
from utils import Point
from math import pi, cos, sin, sqrt
from collections import namedtuple
from gametile import GameTile

canvas_height = 300
canvas_width = 300
_size = 30
hex_width = sqrt(3) * _size
hex_height = 2 * _size
horiz_spacing = hex_width
vert_spacing = hex_height * (3/4)


def main():
    tk = Tk()
    w = Canvas(tk, width=canvas_width, height=canvas_height)
    w.pack()
    center = Point(canvas_width/2, canvas_height/2)
    hex_board = create_board(w, center)

    all_vertices = []
    all_edges = []
    for hexa, obj in hex_board:
        for idx, v in enumerate(hexa.vertices):
            all_vertices.append((v.x, v.y))
            if idx == 5:
                next_v = hexa.vertices[0]
                all_edges.append(((v.x, v.y), (next_v.x, next_v.y)))
            else:
                next_v = hexa.vertices[idx + 1]
                all_edges.append(((v.x, v.y), (next_v.x, next_v.y)))

    unique_vertices = [Point(v[0], v[1]) for v in list(set(all_vertices))]
    unique_edges = [[Point(v[0][0], v[0][1]), Point(v[1][0], v[1][1])] for v in list(set(all_edges))]
    for e in unique_edges:
        one = e[0]
        two = e[1]
        # w.create_line(one.x, one.y, two.x, two.y, fill='blue', activefill='white', width=3)
        w.tag_bind(w.create_line(one.x, one.y, two.x, two.y, fill='blue', activefill='white', width=3),
                   '<ButtonPress-1>', on_object_click)

    for v in unique_vertices:
        top = Point(v.x + 5, v.y + 5)
        bot = Point(v.x - 5, v.y - 5)
        # w.create_oval(top.x, top.y, bot.x, bot.y, fill='red', outline='white', activefill='white')
        w.tag_bind(w.create_oval(top.x, top.y, bot.x, bot.y, fill='red', outline='white', activefill='white'),
                   '<ButtonPress-1>', on_object_click)
    mainloop()


def on_object_click(event):
    print('Got object click', event.x, event.y)
    print(event.widget.find_closest(event.x, event.y))


def create_board(canvas, start):
    offset = (horiz_spacing / 2)
    hexagons = []
    board = [
                create_centered_row(3, -2),
                create_centered_row(4, -1),
                create_centered_row(5, 0),
                create_centered_row(4, 1),
                create_centered_row(3, 2)
            ]
    # coords = []
    # for r in range(0, 5):
    #     if r == 1 or r == 3:
    #         for i in range(0, 4):
    #             coords.append(Point(start.x + offset + horiz_spacing * (i - 2), start.y - vert_spacing ))
    #     else:
    #         if r == 0 or r == 4:
    #             for i in range(1, 4):
    #                 coords.append(Point(start.x + horiz_spacing * (i - 2), start.y - vert_spacing * 2))
    #         else:
    #             for i in range(1, 6):
    #                 coords.append(Point(start.x + horiz_spacing * (i - 3), start.y))

    coords = [Point(start.x - horiz_spacing, start.y - vert_spacing * 2),  # First row
              Point(start.x, start.y - vert_spacing * 2),
              Point(start.x + horiz_spacing, start.y - vert_spacing * 2),
              Point(start.x + offset - horiz_spacing * 2, start.y - vert_spacing),  # Second row
              Point(start.x + offset - horiz_spacing, start.y - vert_spacing),
              Point(start.x + offset, start.y - vert_spacing),
              Point(start.x + offset + horiz_spacing, start.y - vert_spacing),
              Point(start.x - horiz_spacing * 2, start.y),  # Third row
              Point(start.x - horiz_spacing, start.y),
              start,
              Point(start.x + horiz_spacing, start.y),
              Point(start.x + horiz_spacing * 2, start.y),
              Point(start.x + offset - horiz_spacing * 2, start.y + vert_spacing),  # Fourth to last row
              Point(start.x + offset - horiz_spacing, start.y + vert_spacing),
              Point(start.x + offset, start.y + vert_spacing),
              Point(start.x + offset + horiz_spacing, start.y + vert_spacing),
              Point(start.x - horiz_spacing, start.y + vert_spacing * 2),  # Fifth row
              Point(start.x, start.y + vert_spacing * 2),
              Point(start.x + horiz_spacing, start.y + vert_spacing * 2)]
    for idx, c in enumerate(coords):
        g = GameTile(idx + 1, c, _size)
        item = canvas.create_polygon(*g.v_to_arr(), fill='black', outline='white')
        hexagons.append((g, item))

    return hexagons


def create_centered_row(num_hex, y_pos):
    offset = horiz_spacing / 2
    row = []

    start_pos = -int(num_hex / 2)

    if num_hex % 2 == 0:
        start_pos += offset

    for i in range(num_hex):
        x_pos = start_pos + (i * horiz_spacing)
        row.append(Point(x_pos, y_pos))
    return row


# if __name__ == '__main__':
#
#     board = [
#         create_centered_row(3, -2),
#         create_centered_row(4, -1),
#         create_centered_row(5, 0),
#         create_centered_row(4, 1),
#         create_centered_row(3, 2)
#     ]
#
#     for row in board:
#         print(row)


if __name__ == "__main__":
    main()
