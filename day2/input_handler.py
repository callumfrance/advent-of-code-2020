from typing import List


class InputHandler:
    

    def __init__(self, file_path: str):
        self.inputs = self.build_inputs(file_path)

    def build_inputs(self, file_path: str) -> List:
        x = self.retrieve_file_contents(file_path)
        x = self.parse_raw_input(x)
        return x

    @staticmethod
    def retrieve_file_contents(file_path: str) -> List[str]:
        file_contents = list()
        with open(file_path) as fp:
            file_contents = fp.read().splitlines()
        return file_contents

    @staticmethod
    def parse_raw_input(in_file_contents: List[str]) -> List: 
        parsed_lines = list()
        for rawline in in_file_contents:
            rawline_sections = rawline.split(' ')
            if len(rawline_sections) == 3:
                x = list(map(int, rawline_sections[0].split('-')))
                y = rawline_sections[1][:-1]
                parsed_lines.append([x, y, rawline_sections[2]])
            else:
                raise IndexError('rawline_sections should have length of 3')
        return parsed_lines
