from dataclasses import dataclass
from difficulty import Difficulty


@dataclass
class Record:

    def __init__(self, time_to_answer, user_answer, question, difficulty):
        self.time = time_to_answer
        self.answer = user_answer
        self.right_answer = str(question.answer)
        self.question = question.question
        self.difficulty = difficulty

    def __str__(self):
        as_dict = vars(self)
        return str(as_dict)

    right_answer: str
    answer: str
    question: str
    time: float
    difficulty: Difficulty
