from typing import List
import pickle
from record import Record

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

    def get_right_record(self, test_id):
        return [x for x in self.get_records(test_id) if x.answer == x.right_answer]

    def get_right_wrong_ratio(self, test_id: int) -> float:
        right = 0
        total = 0

        for x in self.get_records(test_id):
            total += 1
            if x.answer == x.right_answer:
                right += 1

        if total == 0:
            return 0

        return right / total

    def get_sorted_records(self, test_id: int):
        records = self.get_records(test_id)
        records.sort(key=lambda x: x.time)
        return records

    def get_worst_speed(self, test_id: int) -> Record:
        return self.get_right_record(test_id)[-1]

    def get_best_speed(self, test_id: int) -> Record:
        return self.get_right_record(test_id)[0]

    def get_average_speed(self, test_id: int) -> float:
        records = self.get_right_record(test_id)
        times = [x.time for x in records]
        return sum(times) / len(times)
