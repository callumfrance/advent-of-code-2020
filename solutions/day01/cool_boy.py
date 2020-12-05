from typing import List


class CoolBoy:


    def __init__(self, numerals: List[int]):
        self.part_a_solve = None
        self.numerals = numerals
        self.keyed_numerals = dict()

    def part_a(self) -> int:
        for x in self.numerals:
            self.keyed_numerals[2020 - x] = x

            if x in self.keyed_numerals:
                return x * (2020 - x)
        return -1

    def part_b(self) -> int:
        pass
