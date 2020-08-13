from game_manager import GameManager
from user_input import UserInput
from user_output import UserOutput

def main():
    game_manager = GameManager(UserInput(), UserOutput())
    while True:
        game_manager.is_user_exit()


if __name__ == '__main__':
    main()
