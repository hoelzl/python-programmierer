from othellite.player import Player


def test_player_value():
    # This test is pretty superfluous...
    assert Player.LIGHT.value == 0
    assert Player.DARK.value == 1
