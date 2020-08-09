import game_modeI
from difficulty import Difficulty
from question import Question

class DivisionTest(game_modeI.GameModeI):

    def get_description(self) -> str:
        return "Positive division"

    def get_question(self, difficulty: Difficulty) -> Question:
        numbers = self.generate_numbers(difficulty)

        question = f"What is {numbers[0]} / {numbers[1]}? (two numbers after comma)"

        answer = numbers[0] / numbers[1]
        answer = round(answer, 2)
        return Question(question, answer)
