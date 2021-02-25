from pathlib import Path
from typing import List, Set, NamedTuple, Tuple


class Intersection():
    id: int
    streets: List[Tuple[str, int]]
    total_time: int

    def __init__(self, id, streets):
        self.id = id
        self.streets = streets

        self.total_time = sum([x[1] for x in streets])
        self.streets_len = len(streets)

    def __str__(self):
        string = f"{self.id}\n{len(self.streets)}\n"
        for x in self.streets:
            string += f"{x[0]} {x[1]}\n"
        return string

    def init(self, problem):
        problem.streets[self.streets[0][0]].is_green = True

    def green_light(self, problem, current_time):
        if self.streets_len == 1:
            return

        intersection_time = current_time % self.total_time

        green_street: Street = None
        current_loop_time = 0
        for i, (street_name, green_time) in enumerate(self.streets):
            current_loop_time += green_time
            if current_loop_time > intersection_time:
                break

        green_street = problem.streets[self.streets[(i)%self.streets_len][0]]
        red_street = problem.streets[self.streets[(i-1)%self.streets_len][0]]
        print(f'int {self.id} green lighting {green_street.name}')
        print(f'int {self.id} red lighting {red_street.name}')

        green_street.is_green = True
        red_street.is_green = False

class Solution(NamedTuple):
    intersections: List[Intersection]

    def write_output(self, filepath: Path):
        output_folder: Path = filepath.parent
        if not output_folder.exists():
            output_folder.mkdir(parents=True)
        with filepath.open("w") as fp:
            fp.write(f"{len(self.intersections)}\n")
            for intersection in self.intersections:
                fp.write(str(intersection))


if __name__ == "__main__":
    intersection = Intersection(1, [("rue-d-athenes", 2), ("rue-d-amsterdam", 1)])
    intersection2 = Intersection(0, [("rue-de-londres", 2)])
    intersection3 = Intersection(2, [("rue-de-moscou", 1)])

    solution = Solution([intersection, intersection2, intersection3])
    solution.write_output("result.txt")
