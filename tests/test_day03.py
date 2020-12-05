# day03 tests

import pytest
from os.path import dirname, join

from solutions.day03.input_handler import InputHandler

@pytest.fixture
def day03_resource():
    print("==============================")
    print(__file__)
    print("==============================")
    print(join(dirname(__file__), r"helpers\inputA.txt"))
    print("==============================")
    yield InputHandler(join(dirname(__file__), r"helpers\inputA.txt"))


class TestInputHandler:


    def test_class_build(self, day03_resource):
        assert day03_resource.max_base_col == 0
        assert day03_resource.max_row == 0
        assert day03_resource.grid == dict()
        assert day03_resource.file_path == \
                join(dirname(__file__), r"helpers\inputA.txt")

    def test_build_inputs(self, day03_resource):
        j = day03_resource.build_inputs()
        assert j == \
                {
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
