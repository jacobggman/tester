import game_modeI
from difficulty import Difficulty
from question import Question


class LessTest(game_modeI.GameModeI):

    def get_description(self) -> str:
        return "Positive less"

    def get_question(self, difficulty: Difficulty) -> Question:
        numbers = self.generate_numbers(difficulty)

        question = f"What is {numbers[0]} - {numbers[1]}?"

        answer = numbers[0] - numbers[1]

        return Question(question, answer)
