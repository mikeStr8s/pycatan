from board.board import Board


def main():
    b = Board()
    b.generate_tile_row(3, 0)
    b.generate_tile_row(4, 1)
    b.generate_tile_row(5, 2)
    b.generate_tile_row(4, 3)
    b.generate_tile_row(3, 4)
    print('Done')


if __name__ == '__main__':
    main()
