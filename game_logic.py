from board.board import Board

game_board = None


def game():
    setup()
    print(game_board)


def setup():
    global game_board
    game_board = generate_board()
    resources = ['wood', 'sheep', 'wheat', 'brick', 'stone', 'brick', 'sheep', 'desert', 'wood', 'wheat', 'wood',
                 'wheat', 'brick', 'sheep', 'sheep', 'stone', 'stone', 'wheat', 'wood']
    tile_values = [11, 12, 9, 4, 6, 5, 10, 7, 3, 11, 4, 8, 8, 10, 9, 3, 5, 2, 6]


def generate_board():
    b = Board()
    b.generate_tile_row(3, 0)
    b.generate_tile_row(4, 1)
    b.generate_tile_row(5, 2)
    b.generate_tile_row(4, 3)
    b.generate_tile_row(3, 4)
    return b


if __name__ == '__main__':
    game()
