# day03 tests

import pytest
from os.path import dirname, join

from solutions.day03.input_handler import InputHandler
from solutions.day03.sleddie import Sleddie

TEST_DICT = { \
                (0,0): True,
                (0,1): False,
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
            }

@pytest.fixture
def day03_ih():
    print("==============================")
    print(__file__)
    print("==============================")
    print(join(dirname(__file__), r"helpers\inputA.txt"))
    print("==============================")
    yield InputHandler(join(dirname(__file__), r"helpers\inputA.txt"))

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
                join(dirname(__file__), r"helpers\inputA.txt")

    def test_build_inputs(self, day03_ih):
        j = day03_ih.build_inputs()
        assert j == TEST_DICT


class TestSleddie:


    def test_class_build(self, day03_sleddie):
        assert day03_sleddie.row_size == 1
        assert day03_sleddie.col_size == 5
        assert day03_sleddie.tree_hits == 0
        assert day03_sleddie.map == TEST_DICT
