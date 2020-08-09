from dataclasses import dataclass
from difficulty import Difficulty


@dataclass
class Record:

    def __init__(self):
        pass

    def __str__(self):
        as_dict = vars(self)
        return str(as_dict)

    right_answer: str
    answer: str
    question: str
    time: float
    difficulty: Difficulty
