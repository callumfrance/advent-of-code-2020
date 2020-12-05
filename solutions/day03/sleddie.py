from typing import Dict, List, Tuple


class Sleddie:

    
    def __init__(self, 
            in_map: Dict[Tuple[int, int], bool], 
            rows: int, 
            cols: int,
            slopes: List[Tuple[int, int]]):
        self.row_size = rows
        self.col_size = cols
        self.map = in_map
        self.slopes = slopes
        self.slope_multiple = 0
        self.tree_hits = dict()

    def calc_all_slope_tree_hits(self):
        for x in self.slopes:
            self.calc_tree_hits(x)
        
        for i, x in enumerate(self.tree_hits):
            print("x is ", self.tree_hits[x])
            if i == 0:
                self.slope_multiple = self.tree_hits[x]
            else:
                self.slope_multiple *= self.tree_hits[x]

        return self.slope_multiple

    def calc_tree_hits(self, sloping: Tuple[int, int]) -> int:
        self.tree_hits[sloping] = 0
        current_position = (0, 0)
        
        while current_position != (-1, -1):
            if self.map[current_position]:
                self.tree_hits[sloping] += 1

            current_position = self.get_next_position(sloping, current_position)
        
        return self.tree_hits[sloping]

    def get_next_position(self, 
            sloping: Tuple[int, int], 
            pos: Tuple[int, int]) -> Tuple[int, int]:

        y = (pos[1] + sloping[0]) % (self.col_size + 1)
        if pos[0] + sloping[1] <= self.row_size:
            x = pos[0] + sloping[1]
        else:
            return (-1, -1)
        return (x, y)
