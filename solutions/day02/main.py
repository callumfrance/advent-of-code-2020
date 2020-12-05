#!/usr/bin/env python3

from typing import List
from sys import argv

from input_handler import InputHandler
from password_validator import PasswordValidator

def main(argv: List):
    ih = InputHandler(argv[0])
    v = PasswordValidator(ih.inputs)
    v.calculate_valids()
    print(v.valid_count)


if __name__ == '__main__':
    main(argv[1:])
