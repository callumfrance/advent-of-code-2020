from typing import List


class PasswordValidator:


    def __init__(self, inputs: List):
        self.inputs: List = inputs
        self.valid_count: int = 0

    def calculate_valids(self):
        for x in self.inputs:
#            if self.calculate_valid_summer(x):
#                self.valid_count += 1
            if self.calculate_valid_positioner(x):
                self.valid_count += 1

    @staticmethod
    def calculate_valid_positioner(single: List) -> bool:
        isValid = False
        if single[0][1] > len(single[2]):
            # the final index matcher is greater than entire 1- string
            return isValid
        else:
            setCount = 0
            if single[2][single[0][0] - 1] == single[1]:
                setCount += 1
            if single[2][single[0][1] - 1] == single[1]:
                setCount += 1
            if setCount == 1:
                isValid = True
        return isValid

    @staticmethod
    def calculate_valid_summer(single: List) -> bool:
        isValid = False
        if single[0][0] > len(single[2]):
            # the smallest possible match is greater than entire string
            return isValid
        else:
            matches = single[2].count(single[1])
            if (matches >= single[0][0]) and (matches <= single[0][1]):
                isValid = True
        return isValid
