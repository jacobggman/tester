from typing import Tuple
from difficulty import Difficulty
from question import Question
from generator import Generator


class GameModeI:

    def get_description(self) -> str:
        pass

    def get_question(self, difficulty: Difficulty) -> Question:
        pass

    @staticmethod
    def generate_numbers(difficulty) -> Tuple[int, int]:
        num_of_digits = GameModeI.get_num_digits(difficulty)
        first_num = Generator.positive_num(num_of_digits)
        second_num = Generator.positive_num(num_of_digits)
        return first_num, second_num

    @staticmethod
    def get_num_digits(difficulty: Difficulty) -> int:
        if difficulty == difficulty.EASY:
            return 1
        if difficulty == difficulty.MEDIUM:
            return 3
        if difficulty == difficulty.HARD:
            return 7
