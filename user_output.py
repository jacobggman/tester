

class UserOutput:

    def __init__(self):
        pass

    def record(self, record):
        print(record)

    def records(self, records):
        for r in records:
            self.record(r)

    def float(self, num, info):
        print(round(num, 2), info)

    def no_history(self):
        print("Not have any history")

    def is_right(self, user_answer, right_answer):
        if user_answer == str(right_answer):
            print("RIGHT!")
        else:
            print(f"WRONG. The answer is '{right_answer}'")

    def time_take(self, time):
        print(f"Time take for answering: {round(time, 2)} seconds")

    @staticmethod
    def options(options):
        for i, option in enumerate(options):
            print(i, "for", option)
