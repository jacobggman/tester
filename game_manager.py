from typing import List
from game_modeI import GameModeI
from add_test import AddTest
from difficulty import Difficulty
from user_input import UserInput
# todo
# add more game mode
# better input
# check time
# stats and save best score


class GameManager:

    def __init__(self):
        self.game_modes: List[GameModeI] = [AddTest()]
        while True:
            self.test(self.select_game_mode())

    def select_game_mode(self) -> GameModeI:

        options = [x.get_description() for x in self.game_modes]
        self.print_options(options)
        return self.game_modes[UserInput.get_option_index(options)]

    def test(self, game: GameModeI):
        difficulty = self.get_difficulty()
        while True:
            question = game.get_question(difficulty)
            user_answer = UserInput.get_num(question.question + "\n")
            if user_answer == question.answer:
                print("RIGHT!")
            else:
                print(f"WRONG. the answer is {question.answer}")

            keep_asking = UserInput.get_yes_or_not("do you want to continue?: ")

            if not keep_asking:
                return

    def get_difficulty(self) -> Difficulty:
        options = {
            "easy": Difficulty.EASY,
            "medium": Difficulty.MEDIUM,
            "hard": Difficulty.HARD
        }

        self.print_options(options)
        select_index = UserInput.get_option_index(options.keys())
        return options[list(options)[select_index]]

    def print_options(self, options):
        for i, option in enumerate(options):
            print(i, "for", option)


GameManager()
