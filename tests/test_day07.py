# day07 tests

import pytest
from os.path import dirname, join

from solutions.day07.input_handler import InputHandler
from solutions.day07.haversacks import HaverSacks

INPUT_FILE = r"helpers\input_day07.txt"

TEST_INPUT = None

@pytest.fixture
def day07_ih():
    print("==============================")
    print(__file__)
    print("==============================")
    print(join(dirname(__file__), INPUT_FILE))
    print("==============================")
    yield InputHandler(join(dirname(__file__), INPUT_FILE))


class TestInputHandler:


    def test_class_build(self, day07_ih):
        assert day07_ih.seats == list()
        assert day07_ih.file_path == \
                join(dirname(__file__), INPUT_FILE)

    def test_build_inputs(self, day07_ih):
        j = day07_ih.build_inputs()
        assert j == TEST_INPUT


