from typing import List


class InputHandler:


    def __init__(self, file_path: str):
        self.seats = list()
        self.file_path = file_path

    def build_inputs(self, file_path: str=None) -> List[str]:
        if not file_path:
            file_path = self.file_path
        self.seats = self.retrieve_file_contents(file_path)
        return self.seats

    @staticmethod
    def retrieve_file_contents(file_path: str) -> List[str]:
        file_contents = list()
        with open(file_path) as fp:
            file_contents = fp.read().splitlines()
        return file_contents
