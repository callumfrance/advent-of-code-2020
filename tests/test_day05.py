# day05 tests

import pytest
from os.path import dirname, join

from solutions.day05.input_handler import InputHandler
from solutions.day05.aero import Aero

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


@pytest.fixture
def day05_aero(day05_ih):
    day05_ih.build_inputs()
    yield Aero(day05_ih.seats)

class TestInputHandler:


    def test_class_build(self, day05_ih):
        assert day05_ih.seats == list()
        assert day05_ih.file_path == \
                join(dirname(__file__), INPUT_FILE)

    def test_build_inputs(self, day05_ih):
        j = day05_ih.build_inputs()
        assert j == TEST_INPUT


class TestAero:


    def test_class_build(self, day05_aero):
        assert day05_aero.seat_values == dict()
        assert day05_aero.seats == TEST_INPUT

    def test_seat_value(self, day05_aero):
        assert day05_aero.calc_seat_value('FBFBBFFRLR') == \
                (44, 5, 357)

        assert day05_aero.calc_seat_value(TEST_INPUT[0]) == \
                (82, 0, 656)

        assert day05_aero.calc_seat_value(TEST_INPUT[1]) == \
                (19, 2, 154)

    def test_seat_values(self, day05_aero):
        assert day05_aero.calc_seat_values() == \
                { \
                    656: (82, 0, "BFBFFBFLLL"),
                    154: (19, 2, "FFBFFBBLRL"),
                    165: (20, 5, "FFBFBFFRLR"),
                    185: (23, 1, "FFBFBBBLLR"),
                    105: (13, 1, "FFFBBFBLLR"),
                }

    def test_get_highest_seat_id(self, day05_aero):
        day05_aero.calc_seat_values()
        assert day05_aero.get_highest_seat_id() == 656
