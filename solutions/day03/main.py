#!/usr/bin/env python3

from typing import List
from sys import argv
from os.path import dirname, join

from input_handler import InputHandler
from sleddie import Sleddie

def main(argv: List):
    ih = InputHandler(join(dirname(__file__), argv[0]))
    ih.build_inputs()
    s = Sleddie(ih.grid, ih.max_row, ih.max_base_col)
    s.calc_tree_hits()
    print(s.tree_hits)


if __name__ == '__main__':
    main(argv[1:])
