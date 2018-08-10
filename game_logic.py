from board.board import Board
from random import shuffle

game_board = None
random_start = False  # Default easy setup for the game
num_players = 3  # Default minimum number of players for a game


def game():
    setup()
    print(game_board)


def setup():
    global game_board
    global num_players
    global random_start
    game_board = Board()

    # Default configuration of resources and dice roll values for easy mode
    resources = ['wood', 'sheep', 'wheat', 'brick', 'stone', 'brick', 'sheep', 'desert', 'wood', 'wheat', 'wood',
                 'wheat', 'brick', 'sheep', 'sheep', 'stone', 'stone', 'wheat', 'wood']
    tile_values = [11, 12, 9, 4, 6, 5, 10, 7, 3, 11, 4, 8, 8, 10, 9, 3, 5, 2, 6]

    # If a random board is desired shuffle the lists
    if random_start:
        shuffle(resources)
        shuffle(tile_values)

    # Assign resources and dice roll values to each tile on the board
    for idx, tile_id in enumerate(game_board.tiles):
        coords = tile_id.split('-')
        tile = game_board.get_tile(coords[0], coords[1])
        tile.value = tile_values[idx]
        tile.resource = resources[idx]

    # Create specified number of players
    game_board.create_players(num_players)


if __name__ == '__main__':
    game()
