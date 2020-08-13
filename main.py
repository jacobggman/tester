from game_manager import GameManager
from user_input import UserInput
from user_output import UserOutput

def main():
    input_class = UserInput()
    out_class = UserOutput()
    game_manager = GameManager(input_class, out_class)
    while game_manager.is_run():
        pass


if __name__ == '__main__':
    main()
