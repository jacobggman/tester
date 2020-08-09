import random

class Generator:

    @staticmethod
    def number(len) -> int:
        return random.randrange(-1 * 10**len, 10**len)

    @staticmethod
    def positive_num(len) -> int:
        return random.randrange(1, 10**len)

