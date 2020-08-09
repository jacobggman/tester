from typing import Tuple
import game_modeI
from difficulty import Difficulty
from question import Question
from generator import Generator


class AddTest(game_modeI.GameModeI):

    def get_description(self) -> str:
        return "Positive plus"

    def get_question(self, difficulty: Difficulty) -> Question:
        numbers = self.generate_numbers(difficulty)

        question = f"What is {numbers[0]} + {numbers[1]}?"

        return Question(question, sum(numbers))

    @staticmethod
    def generate_numbers(difficulty) -> Tuple[int, int]:
        num_of_digits = AddTest.get_num_digits(difficulty)
        first_num = Generator.positive_num(num_of_digits)
        second_num = Generator.positive_num(num_of_digits)
        return first_num, second_num

    @staticmethod
    def get_num_digits(difficulty: Difficulty) -> int:
        if difficulty.EASY:
            return 1
        if difficulty.MEDIUM:
            return 3
        if difficulty.HARD:
            return 7
