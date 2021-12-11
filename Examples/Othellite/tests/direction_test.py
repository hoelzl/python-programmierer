from othellite.direction import Direction


def test_abbreviations():
    assert Direction.N is Direction.NORTH
    assert Direction.NE is Direction.NORTH_EAST
    assert Direction.E is Direction.EAST
    assert Direction.SE is Direction.SOUTH_EAST
    assert Direction.S is Direction.SOUTH
    assert Direction.SW is Direction.SOUTH_WEST
    assert Direction.W is Direction.WEST
    assert Direction.NW is Direction.NORTH_WEST
