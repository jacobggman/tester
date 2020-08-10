import game_modeI
from difficulty import Difficulty
from question import Question


class DivisionTest(game_modeI.TestI):

    def get_description(self) -> str:
        return "Positive division"

    def get_divide_no_remainder_numbers(self, difficulty):
        while True:
            numbers = self.generate_numbers(difficulty)
            if numbers[0] % numbers[1] == 0:
                return numbers

    def get_question(self, difficulty: Difficulty) -> Question:
        numbers = self.get_divide_no_remainder_numbers(difficulty)
        question = f"What is {numbers[0]} / {numbers[1]}?"

        answer = numbers[0] // numbers[1]
        answer = round(answer, 2)
        return Question(question, answer)
