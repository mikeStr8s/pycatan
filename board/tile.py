class Tile:
    def __init__(self):
        self.tile_id = None
        self.resource = None
        self.value = None  # Numerical value for dice rolls
        self.vertices = []

    def __and__(self, other):
        assert isinstance(other, Tile)
        if self.tile_id == other.tile_id:
            return True
        else:
            return False
