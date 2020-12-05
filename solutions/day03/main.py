#!/usr/bin/env python3

from typing import List
from sys import argv
from os.path import dirname, join

from input_handler import InputHandler
from sleddie import Sleddie

SLOPES = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
        ]

def main(argv: List):
    ih = InputHandler(join(dirname(__file__), argv[0]))
    ih.build_inputs()
    s = Sleddie(ih.grid, ih.max_row, ih.max_base_col, SLOPES)
    s.calc_all_slope_tree_hits()
    print(s.slope_multiple)


if __name__ == '__main__':
    main(argv[1:])
