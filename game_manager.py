import time
from typing import List, Callable, Tuple
from game_modeI import TestI
from difficulty import Difficulty
from stats import Stats, Record
from test_picker import TestPicker


class GameManager:
    def __init__(self, input_class, output_class):
        self.run = True

        self.input = input_class
        self.output = output_class

        self.test_picker = TestPicker()
        self.stats = Stats()

        self.options_in_test = self.init_test_option()
        self.difficulty_options = self.init_difficulty_options()

    def init_test_option(self):
        return [
            (self.test, "test"),
            (self.best_time, "best_time"),
            (self.worst_time, "worst_time"),
            (self.history, "history"),
            (self.average_time, "average_time"),
            (self.clear_history, "clear"),
            (self.right_wrong, "right, wrong ratio "),
        ]

    def init_difficulty_options(self):
        return [
            (Difficulty.EASY, "easy"),
            (Difficulty.MEDIUM, "medium"),
            (Difficulty.HARD, "hard")
        ]

    def is_run(self) -> bool:
        selected_test = self.select_test()

        selected_func = self.user_select(self.options_in_test)

        self.call_func(selected_func, selected_test)

        return self.run

    def call_func(self, func: Callable[[TestI], None], test: TestI) -> None:
        try:
            func(test)
        except (FileNotFoundError, IndexError):
            self.output.no_history()

    def select_test(self) -> TestI:
        options = self.test_picker.get_test_option()
        return self.user_select(options)

    def user_select(self, options: List[Tuple[any, str]]) -> any:
        self.out_msgs(options)
        value, msg = self.select_option(options)
        return value

    def out_msgs(self, options: List[Tuple[any, str]]) -> None:
        msgs = [msg for _, msg in options]
        self.output.options(msgs)

    def select_option(self, options: List[Tuple[any, str]]) -> any:
        user_index = self.input.get_option_index(options)
        select_tuple = options[user_index]
        return select_tuple

    def test(self, game: TestI) -> None:
        difficulty = self.get_difficulty()

        while True:
            record = self.get_answer_record(game, difficulty)

            self.stats.save(record, game.test_id)

            keep_asking = self.input.get_yes_or_not("Do you want to continue?: ")

            if not keep_asking:
                return

    def get_difficulty(self) -> Difficulty:
        options = self.difficulty_options
        return self.user_select(options)

    def get_answer_record(self, game: TestI, difficulty: Difficulty) -> Record:
        question = game.get_question(difficulty)

        user_answer, time_to_answer = self.handle_user_answer(question)

        record = Record(time_to_answer, user_answer, question, difficulty)

        return record

    def handle_user_answer(self, question) -> Tuple[str, float]:
        question_text = question.question
        user_answer, time_to_answer = self.get_answer_data(question_text)

        self.output.is_right(user_answer, question.answer)
        self.output.time_take(time_to_answer)

        return user_answer, time_to_answer

    def get_answer_data(self, question: str) -> Tuple[str, float]:
        time_before = time.time()
        user_answer = self.input.get_answer(question)
        time_to_answer = time.time() - time_before
        return user_answer, time_to_answer

    def best_time(self, game: TestI) -> None:
        record = self.stats.get_best_speed(game.test_id)
        self.output.record(record)

    def worst_time(self, game: TestI) -> None:
        record = self.stats.get_worst_speed(game.test_id)
        self.output.record(record)

    def history(self, game: TestI) -> None:
        records = self.stats.get_records(game.test_id)
        self.output.records(records)

    def average_time(self, game: TestI) -> None:
        average = self.stats.get_average_speed(game.test_id)
        self.output.float(average, "Seconds")

    def clear_history(self, game: TestI) -> None:
        if self.input.get_yes_or_not("Are you sure?: "):
            self.stats.clear_test(game.test_id)

    def right_wrong(self, game: TestI) -> None:
        ratio = self.stats.get_right_wrong_ratio(game.test_id)
        self.output.float(ratio, "Right Ratio")
