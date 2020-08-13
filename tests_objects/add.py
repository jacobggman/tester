import test_interface
from difficulty import Difficulty
from question import Question


class AddTest(test_interface.TestI):

    def get_description(self) -> str:
        return "Positive plus"

    def get_question(self, difficulty: Difficulty) -> Question:
        numbers = self.generate_numbers(difficulty)

        question = f"What is {numbers[0]} + {numbers[1]}?"

        return Question(question, sum(numbers))
