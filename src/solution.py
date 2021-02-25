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


if __name__ == "__main__":
    intersection = Intersection(1, [("rue-d-athenes", 2), ("rue-d-amsterdam", 1)])
    intersection2 = Intersection(0, [("rue-de-londres", 2)])
    intersection3 = Intersection(2, [("rue-de-moscou", 1)])

    solution = Solution([intersection, intersection2, intersection3])
    solution.write_output("result.txt")
