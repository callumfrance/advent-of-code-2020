from typing import Dict, List

from haversacks import HaverSack


class InputHandler:


    def __init__(self, file_path: str):
        self.haversacks = Dict[str, List]
        self.file_path = file_path

    def build_inputs(self, file_path: str=None) -> Dict[str, List]:
        if not file_path:
            file_path = self.file_path
        self.haversacks = self.retrieve_file_contents(file_path)

        return self.haversacks

    @staticmethod
    def retrieve_file_contents(file_path: str) -> Dict[str, HaverSack]:
        file_contents = dict()
        with open(file_path) as fp:
            x = fp.read().split(' bags contain ')
            j = HaverSack(x[0])
            k = list()
            if x[1] == 'no other bags':
                pass
            else:
                k = x[1].split(', ')
                k[-1] = k[-1][:-1]
                for s in k:
                    count = int(s.split(' ')[0])
                    name = s.split(' ')[1:]
                    j.add_child(HaverSack(name=name, parents=(j)), count)
            file_contents[j.name] = j
        return file_contents
