import time
from typing import List, Callable
from game_modeI import TestI
from difficulty import Difficulty
from user_input import UserInput
from stats import Stats, Record
from tests.add import AddTest
from tests.less import LessTest
from tests.division import DivisionTest
from tests.multiply import MultiplyTest

# todo
# add and fix clear
# fix history
# fix record print
# count only right answers
# right / wrong ratio
# add difficulty option to all
# make record in his oun file
# make sure that have record
# make function shorts
# rename and vars
# play!


class GameManager:

    def __init__(self):
        self.tests_modes: List[TestI] = [
            AddTest(),
            LessTest(),
            DivisionTest(),
            MultiplyTest()
        ]

        self.test_option: List[Callable[[TestI], None]] = [
            self.test,
            self.best_time,
            self.worst_time,
            self.history,
            self.average_time,
            self.clear_history
        ]

        self.init_tests_id()

        self.stats = Stats()

        self.run = True

    def init_tests_id(self):
        for i, x in enumerate(self.tests_modes):
            x.test_id = i

    def best_time(self, game: TestI):
        print(self.stats.get_best_speed(game.test_id))

    def worst_time(self, game: TestI):
        print(self.stats.get_worst_speed(game.test_id))

    def history(self, game: TestI):
        print(self.stats.get_records(game.test_id)[::-1])

    def average_time(self, game: TestI):
        print(self.stats.get_average_speed(game.test_id))

    def clear_history(self, game: TestI):
        self.stats.clear_test(game.test_id)

    def is_user_exit(self) -> bool:
        selected_test = self.select_test()

        options = ["test", "best_time", "worst_time", "history", "average_time", "clear"]
        self.print_options(options)
        user_index = UserInput.get_option_index(self.test_option)

        func = self.test_option[user_index]

        func(selected_test)

        return not self.run

    def select_test(self) -> TestI:

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

            record = Record()
            record.time = time_to_answer
            record.answer = user_answer
            record.right_answer = str(question.answer)
            record.question = question
            record.difficulty = difficulty
            self.stats.save(record, game.test_id)
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

    # todo better select and print options
    @staticmethod
    def print_options(options):
        for i, option in enumerate(options):
            print(i, "for", option)
