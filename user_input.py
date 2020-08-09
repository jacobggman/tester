
class UserInput:

    @staticmethod
    def get_num(msg):
        while True:
            try:
                user_input = input(msg)
                num_as_input = int(user_input)
                return num_as_input
            except ValueError:
                continue

    @staticmethod
    def get_range(between: range) -> int:
        while True:
            msg = f"Enter number between {between.start} and {between.stop - 1}: "
            try:
                num_as_input = UserInput.get_num(msg)
                if num_as_input in between:
                    return num_as_input
            except ValueError:
                continue

    @staticmethod
    def get_option_index(options: iter) -> int:
        option_num = len(options)
        num_game_modes = range(option_num)

        select_index = UserInput.get_range(num_game_modes)
        return select_index

    @staticmethod
    def get_yes_or_not(msg) -> bool:
        while True:
            user_input = input(msg)
            if len(user_input) == 0:
                return True
            first_letter_input = user_input[0].lower()
            if first_letter_input in ("y", "1"):
                return True
            if first_letter_input in ("n", "0"):
                return False
