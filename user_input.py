

class UserInput:

    def __init__(self):
        self.YES_CHARS = ("y", "1")
        self.NO_CHARS = ("n", "0")

    def get_num(self, msg):
        while True:
            try:
                user_input = input(msg)
                num_as_input = int(user_input)
                return num_as_input
            except ValueError:
                continue

    def get_range(self, between: range) -> int:
        while True:
            msg = f"Enter number between {between.start} and {between.stop - 1}: "
            try:
                num_as_input = self.get_num(msg)
                if num_as_input in between:
                    return num_as_input
            except ValueError:
                continue

    def get_option_index(self, options: iter) -> int:
        option_num = len(options)
        num_game_modes = range(option_num)

        select_index = self.get_range(num_game_modes)
        return select_index

    def get_yes_or_not(self, msg) -> bool:
        while True:
            user_input = input(msg)
            if len(user_input) == 0:
                return True
            first_letter_input = user_input[0].lower()
            if first_letter_input in self.YES_CHARS:
                return True
            if first_letter_input in self.NO_CHARS:
                return False

    def get_answer(self, question) -> str:
        return input(question + "\n")
