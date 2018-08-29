from board.board import Board
from random import shuffle, SystemRandom
from tkinter import *


def game():
    setup()


def setup():
    random_start = False  # Default easy setup for the game
    num_players = 3  # Default minimum number of players for a game
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

    master = Tk()
    canvas = Canvas(master, width=game_board.side_length, height=game_board.side_length)
    canvas.pack()
    for tile in game_board.tiles:
        coords = tile.split('-')
        t = game_board.get_tile(coords[0], coords[1])
        canvas.create_polygon(*t.vertices_to_list(), fill=t.get_color(), outline='white')

    mainloop()


def roll_dice():
    return SystemRandom().randint(2, 12)


def gather_resources(board, dice_roll):
    for settlement in board.settlements:
        for tile in settlement.vertex.tiles:
            if tile.value == dice_roll:
                settlement.player.resources[tile.resource] += 1


def take_turn(player, board):
    """
    The idea for this function is that it will handle taking a single players turn.
    1) Player MUST roll dice. This must occur before any other action on the turn
    2a) Player may choose to trade
    2b) Player may choose to build
    2c) Player may choose to buy development cards
    2d) Player may choose to play development cards
    3) Player ends turn

    NOTE: A player may choose to do any or all of the selections in step 2

    :param player: Player Object for the current player taking the turn
    :param board: Board Object representing the current state of the game board
    :return:
    """
    dice_roll = roll_dice()
    gather_resources(board, dice_roll)
    # TODO: Finish this


if __name__ == '__main__':
    game()
