import time
from typing import List, Callable, Tuple
from game_modeI import TestI
from difficulty import Difficulty
from user_input import UserInput
from stats import Stats, Record
from test_picker import TestPicker
from user_output import UserOutput

# todo
# add difficulty option to all
# make different screen for stats
# play!
# separate the input and output


class GameManager:

    def __init__(self):

        self.test_picker = TestPicker()

        self.out = UserOutput()

        self.options_in_test: List[Tuple[Callable[[TestI], None], str]] = [
            (self.test, "test"),
            (self.best_time, "best_time"),
            (self.worst_time, "worst_time"),
            (self.history, "history"),
            (self.average_time, "average_time"),
            (self.clear_history, "clear"),
            (self.right_wrong, "right, wrong ratio "),
        ]

        self.init_tests_id()

        self.stats = Stats()

        self.run = True

    def init_tests_id(self):
        for i, value_tuple in enumerate(self.test_picker.get_test_option()):
            test_object = value_tuple[0]
            test_object.test_id = i

    def best_time(self, game: TestI):
        record = self.stats.get_best_speed(game.test_id)
        self.out.record(record)

    def worst_time(self, game: TestI):
        record = self.stats.get_worst_speed(game.test_id)
        self.out.record(record)

    def history(self, game: TestI):
        records = self.stats.get_records(game.test_id)
        self.out.records(records)

    def average_time(self, game: TestI):
        average = self.stats.get_average_speed(game.test_id)
        self.out.float(average, "Seconds")

    def clear_history(self, game: TestI):
        if UserInput.get_yes_or_not("Are you sure?: "):
            self.stats.clear_test(game.test_id)

    def right_wrong(self, game: TestI):
        ratio = self.stats.get_right_wrong_ratio(game.test_id)
        self.out.float(ratio, "Right Ratio")

    def is_user_exit(self) -> bool:
        selected_test = self.select_test()

        func = self.user_select(self.options_in_test)

        try:
            func(selected_test)
        except (FileNotFoundError, IndexError):
            self.out.no_history()

        return not self.run

    def select_test(self) -> TestI:
        return self.user_select(self.test_picker.get_test_option())

    def user_select(self, options: List[Tuple[any, str]]) -> any:
        self.out.options([msg for _, msg in options])
        return options[UserInput.get_option_index(options)][0]

    def handle_user_answer(self, question):
        time_before = time.time()
        user_answer = UserInput.get_answer(question.question)
        time_to_answer = time.time() - time_before

        self.out.is_right(user_answer, question.answer)

        self.out.time_take(time_to_answer)

        return user_answer, time_to_answer

    def test(self, game: TestI):
        difficulty = self.get_difficulty()

        while True:
            question = game.get_question(difficulty)

            user_answer, time_to_answer = self.handle_user_answer(question)

            record = Record(time_to_answer, user_answer, question, difficulty)

            self.stats.save(record, game.test_id)

            keep_asking = UserInput.get_yes_or_not("Do you want to continue?: ")

            if not keep_asking:
                return

    def get_difficulty(self) -> Difficulty:
        difficulty_options = [
            (Difficulty.EASY, "easy"),
            (Difficulty.MEDIUM, "medium"),
            (Difficulty.HARD, "hard")
        ]

        return self.user_select(difficulty_options)
