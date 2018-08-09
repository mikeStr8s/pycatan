from board.board import Board

game_board = None
resource_distribution = None
value_distribution = None


def setup():
    global game_board
    global resource_distribution
    global value_distribution
    game_board = generate_board()
    resource_distribution = {
        'wheat': 4,
        'brick': 3,
        'wood': 4,
        'stone': 3,
        'sheep': 4
    }
    value_distribution = {
        2: 1,
        3: 2,
        4: 2,
        5: 2,
        6: 2,
        7: 1,
        8: 2,
        9: 2,
        10: 2,
        11: 2,
        12: 1
    }


def game():
    setup()
    print(game_board)


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
