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

    def set_val(self, value):
        assert isinstance(value, int)
        self.value = value

    def vertices_to_list(self):
        v_list = []
        for v in self.vertices:
            v_list.append(v.coordinates[0])
            v_list.append(v.coordinates[1])
        return v_list
