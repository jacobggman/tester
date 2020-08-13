from typing import List, Tuple
from test_interface import TestI
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

        self.init_tests_id()

    def init_tests_id(self):
        tests_tuple = self.get_test_option()
        for i, value_tuple in enumerate(tests_tuple):
            test_object, description = value_tuple
            test_object.test_id = i

    def get_test_option(self):
        return self.tests_option
