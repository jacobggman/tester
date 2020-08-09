from typing import List
import pickle

class Record:
    right_answer: str
    answer: str
    question: str
    time: float

class Stats:
    def save(self, record: Record, test_id: int):
        file_name = self.get_file_name(test_id)
        f = open(file_name, 'wb')
        pickle.dump(record, f)
        f.close()

    def get_file_name(self, test_id: int):
        return "test" + str(test_id) + ".p"

    def reset_all(self, tests_num: int):
        for x in range(tests_num):
            file_name = self.get_file_name(x)
            self.clear_file(file_name)

    def clear_file(self, file_name):
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