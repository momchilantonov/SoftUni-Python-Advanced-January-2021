from tic_tac_toe_live_demo import setup
from tic_tac_toe_live_demo.play_engine import play


if __name__ == "__main__":
    setup.setup()
    play()
    new_game = input(f"Do you want to play a new game? y/n: ")
    while new_game == "y":
        play()
        new_game = input(f"Do you want to play a new game? y/n: ")

    print(setup.game_counter)
    print("Bye!")
