from difficulty import Difficulty
from question import Question
from tests_objects.division import DivisionTest

class PercentageTest(DivisionTest):

    def get_description(self) -> str:
        return "Percentage"

    def get_present(self, big, small):
        return round(small / big * 100, 2)

    def get_question(self, difficulty: Difficulty) -> Question:
        # answer = numbers*(present/100)
        numbers = self.get_divide_no_remainder_numbers(difficulty)
        present = self.get_present(*numbers)
        big_num, small = numbers
        question = f"How much %{present} of {big_num}?"

        answer = small
        return Question(question, answer)
