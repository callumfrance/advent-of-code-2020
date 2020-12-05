# day01 tests

import pytest
from os.path import dirname, join

from solutions.day01.input_handler import InputHandler
from solutions.day01.cool_boy import CoolBoy

TEST_NUMERALS = [333, 666, 999, 1021]
TEST_NUMERALS_A = [999, 1021]
TEST_NUMERALS_B = [333, 666, 1021]

INPUT_FILE = r"helpers\inputB.txt"

@pytest.fixture
def day01_ih():
    print("==============================")
    print(__file__)
    print("==============================")
    print(join(dirname(__file__), INPUT_FILE))
    print("==============================")
    yield InputHandler(join(dirname(__file__), INPUT_FILE))

@pytest.fixture
def day01_coolboy(day01_ih):
    day01_ih.build_inputs()
    yield CoolBoy(day01_ih.numerals)


class TestInputHandler:


    def test_class_build(self, day01_ih):
        assert day01_ih.numerals == list()
        assert day01_ih.file_path == \
                join(dirname(__file__), INPUT_FILE)

    def test_build_inputs(self, day01_ih):
        j = day01_ih.build_inputs()
        assert j == TEST_NUMERALS
        assert day01_ih.numerals == TEST_NUMERALS


class TestCoolBoy:


    def test_cool_boy_a(self, day01_coolboy):
        assert day01_coolboy.part_a() == (999 * 1021)

    def test_cool_boy_b(self, day01_coolboy):
        assert day01_coolboy.part_b() == (333 * 666 * 1021)
