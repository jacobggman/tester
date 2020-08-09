from difficulty import Difficulty
from question import Question

class GameModeI:

    def get_description(self) -> str:
        pass

    def get_question(self, difficulty: Difficulty) -> Question:
        pass

