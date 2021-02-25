from typing import List, Set, NamedTuple, Tuple


class Intersection(NamedTuple):
    id: int
    streets: List[Tuple[str, int]]

    def __str__(self):
        string = f"{self.id}\n{len(self.streets)}\n"
        for x in self.streets:
            string += f"{x[0]} {x[1]}\n"
        return string


class Solution(NamedTuple):
    intersections: List[Intersection]

    def write_output(self, filename):
        with open(filename, "w") as file:
            file.write(f"{len(self.intersections)}\n")
            for intersection in self.intersections:
                file.write(str(intersection))
