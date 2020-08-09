import time
from typing import List
from game_modeI import TestI
from difficulty import Difficulty
from user_input import UserInput
from tests.add import AddTest
from tests.less import LessTest
from tests.division import DivisionTest
from tests.multiply import MultiplyTest
# todo
# stats and save best score


class GameManager:

    def __init__(self):
        self.tests_modes: List[TestI] = [
            AddTest(),
            LessTest(),
            DivisionTest(),
            MultiplyTest()
        ]

        self.init_tests_id()

    def init_tests_id(self):
        for i, x in enumerate(self.tests_modes):
            x.test_id = i

    def make_test(self):
        return self.test(self.select_game_mode())

    def select_game_mode(self) -> TestI:

        options = [x.get_description() for x in self.tests_modes]
        self.print_options(options)
        return self.tests_modes[UserInput.get_option_index(options)]

    def test(self, game: TestI):
        difficulty = self.get_difficulty()

        while True:
            question = game.get_question(difficulty)
            time_before = time.time()
            user_answer = input(question.question + "\n")
            time_to_answer = time.time() - time_before
            if user_answer == str(question.answer):
                print("RIGHT!")
            else:
                print(f"WRONG. the answer is '{question.answer}'")
            print(f"time take for answering: {round(time_to_answer, 2)} seconds")
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

    @staticmethod
    def print_options(options):
        for i, option in enumerate(options):
            print(i, "for", option)
