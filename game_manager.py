from typing import List
from game_modeI import GameModeI
from add_test import AddTest
from difficulty import Difficulty

class GameManager:

    def __init__(self):
        self.game_modes: List[GameModeI] = [AddTest()]
        self.select_game_mode()

    def select_game_mode(self) -> GameModeI:
        for i, x in enumerate(self.game_modes):
            print(i, "for", x.get_description())

        num_game_modes = range(len(self.game_modes))

        select_index = self.input_in_range(num_game_modes)
        return self.game_modes[select_index]

    def input_in_range(self, between: range) -> int:
        while True:
            msg = f"enter number between {between.start} and {between.stop - 1}: "
            try:
                num_as_input = self.get_num(msg)
                if num_as_input in between:
                    return num_as_input
            except ValueError:
                continue

    def get_num(self, msg):
        while True:
            try:
                num_as_input = int(input(msg))
                return num_as_input
            except ValueError:
                continue

    def test(self, game: GameModeI):
        pass

    def get_difficulty(self) -> Difficulty:
        options = {
        "easy": Difficulty.EASY,
        "medium": Difficulty.MEDIUM,
        "hard": Difficulty.HARD
        }
        option = self.get_option(list(options.keys()))

        return options[option]

    def get_option(self, options):
        self.print_options(options)

        num_game_modes = range(len(options))

        select_index = self.input_in_range(num_game_modes)
        return options[select_index]

    def print_options(self, options):
        for i, option in enumerate(options):
            print(i, "for", option)

print(type(Difficulty.HARD))
print(type(Difficulty))
GameManager()
