from typing import Dict, Tuple, List


class Aero:


    def __init__(self, seats: List[str]):
        self.seats: List[str] = seats
        self.seat_values: Dict[int, Tuple[int, int, str]] = dict()

    def get_highest_seat_id(self) -> int:
        return max(self.seat_values)

    def calc_seat_values(self) -> Dict[int, Tuple[int, int, str]]:
        for seat in self.seats:
            x = self.calc_seat_value(seat)
            self.seat_values[x[2]] = (x[0], x[1], seat)

        return self.seat_values

    @staticmethod
    def calc_seat_value(seat_str) -> Tuple[int, int, int]:
        (row_min, row_max) = (0, 127)
        (col_min, col_max) = (0, 7)
        for i, c in enumerate(seat_str):
            if c == 'F':
                row_max = row_max - (2 ** (6 - i))
            elif c == 'B':
                row_min = row_min + (2 ** (6 - i))
            elif c == 'R':
                col_min = col_min + (2 ** (9 - i))
            elif c == 'L':
                col_max = col_max - (2 ** (9 - i))

        return (row_min, col_min, ((row_min * 8) + col_min))
