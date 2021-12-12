from ..player.random_player import RandomPlayer
from ..game import GameImplementation


def main():
    player1 = RandomPlayer()
    player2 = RandomPlayer()
    game = GameImplementation((player1, player2))
    game.new_game()
    game.run_game_loop()

    print("Hello world from Othellite (cli version).")


if __name__ == "__main__":
    main()
