# day01 tests

import pytest
from os.path import dirname, join

from solutions.day01.input_handler import InputHandler

TEST_NUMERALS = [999, 1021]

INPUT_FILE = r"helpers\inputB.txt"

@pytest.fixture
def day01_ih():
    print("==============================")
    print(__file__)
    print("==============================")
    print(join(dirname(__file__), INPUT_FILE))
    print("==============================")
    yield InputHandler(join(dirname(__file__), INPUT_FILE))


class TestInputHandler:


    def test_class_build(self, day01_ih):
        assert day01_ih.numerals == list()
        assert day01_ih.file_path == \
                join(dirname(__file__), INPUT_FILE)

    def test_build_inputs(self, day01_ih):
        j = day01_ih.build_inputs()
        assert j == TEST_NUMERALS
