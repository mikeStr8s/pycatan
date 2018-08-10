from board.board import Board, PlacementException


def test_place_settlement():
    b = Board()
    b.create_players(3)
    t = b.get_tile(0, 0)
    v1 = t.vertices[0]
    v2 = t.vertices[2]

    b.place_settlement(v1, b.players[0])
    assert len(b.settlements) == 1, 'Expected one successful settlement placements'
    b.place_settlement(v2, b.players[2])
    assert len(b.settlements) == 2, 'Expected two successful settlement placements'


def test_place_settlement_adjacent():
    b = Board()
    b.create_players(3)
    t = b.get_tile(0, 0)
    v1 = t.vertices[0]
    v2 = t.vertices[1]

    b.place_settlement(v1, b.players[0])
    try:
        b.place_settlement(v2, b.players[1])
    except PlacementException:
        assert True
    else:
        assert False, 'Expected Placement Exception for adjacent vertices'
