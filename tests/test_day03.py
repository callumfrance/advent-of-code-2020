# day03 tests

import pytest
from os.path import dirname, join

from solutions.day03.input_handler import InputHandler
from solutions.day03.sleddie import Sleddie

INPUT_FILE = r"helpers\input_day03.txt"

TEST_DICT = { \
                (0,0): False,
                (0,1): True,
                (0,2): True,
                (0,3): False,
                (0,4): False,
                (0,5): True,
                (1,0): False,
                (1,1): True,
                (1,2): False,
                (1,3): False,
                (1,4): False,
                (1,5): True,
                (2,0): True,
                (2,1): False,
                (2,2): True,
                (2,3): False,
                (2,4): False,
                (2,5): True,
            }

@pytest.fixture
def day03_ih():
    print("==============================")
    print(__file__)
    print("==============================")
    print(join(dirname(__file__), INPUT_FILE))
    print("==============================")
    yield InputHandler(join(dirname(__file__), INPUT_FILE))

@pytest.fixture
def day03_sleddie(day03_ih):
    yield Sleddie(day03_ih.build_inputs(),
            day03_ih.max_row,
            day03_ih.max_base_col,
            )

class TestInputHandler:


    def test_class_build(self, day03_ih):
        assert day03_ih.max_base_col == 0
        assert day03_ih.max_row == 0
        assert day03_ih.grid == dict()
        assert day03_ih.file_path == \
                join(dirname(__file__), INPUT_FILE)

    def test_build_inputs(self, day03_ih):
        j = day03_ih.build_inputs()
        assert j == TEST_DICT


class TestSleddie:


    def test_class_build(self, day03_sleddie):
        assert day03_sleddie.row_size == 2
        assert day03_sleddie.col_size == 5
        assert day03_sleddie.tree_hits == 0
        assert day03_sleddie.map == TEST_DICT

    def test_next_position(self, day03_sleddie):
        y = day03_sleddie.get_next_position((0, 0))
        assert y == (1, 3)

        y = day03_sleddie.get_next_position(y)
        assert y == (2, 0)

        y = day03_sleddie.get_next_position(y)
        assert y == (-1, -1)

    def test_calc_tree_hits(self, day03_sleddie):
        x = day03_sleddie.calc_tree_hits()
        assert x == 1
