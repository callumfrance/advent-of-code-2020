#!/usr/bin/env python3

from typing import List
from sys import argv

from input_handler import InputHandler
from sleddie import Sleddie

def main(argv: List):
    ih = InputHandler(argv[0])
    s = Sleddie(ih.grid, ih.max_row, ih.max_base_col)
    s.next_step()
    print(s.tree_hits)


if __name__ == '__main__':
    main(argv[1:])
