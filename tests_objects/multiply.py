import test_interface
from difficulty import Difficulty
from question import Question


class MultiplyTest(test_interface.TestI):

    def get_description(self) -> str:
        return "Positive multiply"

    def get_question(self, difficulty: Difficulty) -> Question:
        numbers = self.generate_numbers(difficulty)

        question = f"What is {numbers[0]} * {numbers[1]}?"

        answer = numbers[0] * numbers[1]

        return Question(question, answer)
