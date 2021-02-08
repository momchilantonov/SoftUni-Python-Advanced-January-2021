from tic_tac_toe.setup import setup_players, setup_board
from tic_tac_toe.logic import play


def setup():
    setup_players()
    setup_board()


if __name__ == "__main__":
    setup()
    play()
