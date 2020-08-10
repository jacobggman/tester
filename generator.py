import random


class Generator:

    @staticmethod
    def number(digit_len) -> int:
        return random.randrange(-1 * 10**digit_len, 10**digit_len)

    @staticmethod
    def positive_num(digit_len) -> int:
        return random.randrange(1, 10**digit_len)
