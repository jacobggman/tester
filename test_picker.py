from typing import List, Tuple
from game_modeI import TestI
from tests_objects.add import AddTest
from tests_objects.less import LessTest
from tests_objects.division import DivisionTest
from tests_objects.multiply import MultiplyTest
from tests_objects.percentage import PercentageTest


class TestPicker:
    def __init__(self):
        tests = [
            AddTest(),
            LessTest(),
            DivisionTest(),
            MultiplyTest(),
            PercentageTest(),
        ]

        self.tests_option: List[Tuple[TestI, str]] = []

        for test in tests:
            self.tests_option.append((test, test.get_description()))

    def get_test_option(self):
        return self.tests_option
