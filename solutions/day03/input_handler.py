from typing import Dict, Tuple, List


class InputHandler:
    """
    self.grid Dict[Tuple, bool]
        A list of cells, with row and modulo column 
    """


    def __init__(self, file_path: str):
        self.max_base_col = 0
        self.max_row = 0
        self.grid = dict()
        self.file_path = file_path

    def build_inputs(self, file_path: str=None) -> Dict[Tuple[int, int], bool]:
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
            -> Dict[Tuple[int, int], bool]:
        self.grid = dict()
        for i, rawline in enumerate(in_file_contents):
            for j, line_char in enumerate(rawline):
                if i == 0:
                    self.max_base_col = j
                if line_char == '.':
                    self.grid[(i, j)] = False
                elif line_char == '#':
                    self.grid[(i, j)] = True
                else:
                    raise TypeError('this character is whack ' + line_char) 
            self.max_row = i
        return self.grid
