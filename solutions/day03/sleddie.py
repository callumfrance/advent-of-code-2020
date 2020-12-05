from typing import Dict, List, Tuple, Union


class Sleddie:

    
    def __init__(self, in_map: Dict[Tuple[int, int], bool], rows: int, cols: int):
        self.row_size = rows
        self.col_size = cols
        self.map = in_map
        self.tree_hits = 0

    def calc_tree_hits(self):
        current_position = (0, 0)
        
        while current_position != (-1, -1):
            if self.map[current_position]:
                self.tree_hits += 1

            current_position = self.get_next_position(current_position)
        
        return self.tree_hits

    def get_next_position(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        y = (pos[1] + 3) % (self.col_size + 1)
        if pos[0] + 1 <= self.row_size:
            x = pos[0] + 1
        else:
            return (-1, -1)
        return (x, y)
