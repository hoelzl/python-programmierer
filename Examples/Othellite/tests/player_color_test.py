from othellite.player_color import PlayerColor


def test_player_value():
    # This test is pretty superfluous...
    assert PlayerColor.LIGHT.value == 0
    assert PlayerColor.DARK.value == 1
