from typing import List


class InputHandler:


    def __init__(self, file_path: str):
        self.numerals = list()
        self.file_path = file_path

    def build_inputs(self, file_path: str=None) -> List[int]:
        if not file_path:
            file_path = self.file_path
        x = self.retrieve_file_contents(file_path)
        x = self.parse_raw_input(x)
        return x

    @staticmethod
    def retrieve_file_contents(file_path: str) -> List[str]:
        file_contents = list()
        with open(file_path) as fp:
            file_contents = fp.read().splitlines()
        return file_contents

    def parse_raw_input(self, in_file_contents: List[str]) \
            -> List[int]:
        self.numerals = list()
        for rawline in in_file_contents:
            try:
                self.numerals.append(int(rawline))
            except:
                raise TypeError('this character is int-able ' + rawline) 

        return self.numerals
