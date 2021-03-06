#!/usr/bin/env python3

from typing import List
from sys import argv
from os.path import dirname, join

from input_handler import InputHandler
from cool_boy import CoolBoy

def main(argv: List):
    ih = InputHandler(join(dirname(__file__), argv[0]))
    ih.build_inputs()
    cb = CoolBoy(ih.numerals)
    print(cb.part_a())
    print(cb.part_b())


if __name__ == '__main__':
    main(argv[1:])
