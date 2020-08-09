from typing import List
from dataclasses import dataclass
import pickle
from difficulty import Difficulty


@dataclass
class Record:

    def __init__(self):
        pass

    right_answer: str
    answer: str
    question: str
    time: float
    difficulty: Difficulty


class Stats:
    def save(self, record: Record, test_id: int):
        file_name = self.get_file_name(test_id)
        f = open(file_name, 'ab')
        pickle.dump(record, f)
        f.close()

    @staticmethod
    def get_file_name(test_id: int):
        return "test" + str(test_id) + ".p"

    def reset_all(self, tests_num: int):
        for x in range(tests_num):
            file_name = self.get_file_name(x)
            self.clear_file(file_name)

    def clear_test(self, test_id: int):
        self.clear_file(self.get_file_name(test_id))

    @staticmethod
    def clear_file(file_name):
        open(file_name, 'w').close()

    def get_records(self, test_id) -> List[Record]:
        records = []

        file_name = self.get_file_name(test_id)
        f = open(file_name, 'rb')

        while True:
            try:
                records.append(pickle.load(f))
            except EOFError:
                break

        f.close()

        return records

    def get_sorted_records(self, test_id: int):
        records = self.get_records(test_id)
        records.sort(key=lambda x: x.time)
        return records

    def get_worst_speed(self, test_id: int) -> Record:
        return self.get_sorted_records(test_id)[-1]

    def get_best_speed(self, test_id: int) -> Record:
        return self.get_sorted_records(test_id)[0]

    def get_average_speed(self, test_id: int) -> float:
        records = self.get_records(test_id)
        times = [x.time for x in records]
        return sum(times) / len(times)
