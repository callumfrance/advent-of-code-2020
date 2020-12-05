# day05 tests

import pytest
from os.path import dirname, join

from solutions.day05.input_handler import InputHandler

INPUT_FILE = r"helpers\input_day05.txt"

TEST_INPUT = [ \
                "BFBFFBFLLL",
                "FFBFFBBLRL",
                "FFBFBFFRLR",
                "FFBFBBBLLR",
                "FFFBBFBLLR",
            ]

@pytest.fixture
def day05_ih():
    print("==============================")
    print(__file__)
    print("==============================")
    print(join(dirname(__file__), INPUT_FILE))
    print("==============================")
    yield InputHandler(join(dirname(__file__), INPUT_FILE))


class TestInputHandler:


    def test_class_build(self, day05_ih):
        assert day05_ih.seats == list()
        assert day05_ih.file_path == \
                join(dirname(__file__), INPUT_FILE)

    def test_build_inputs(self, day05_ih):
        j = day05_ih.build_inputs()
        assert j == TEST_INPUT
