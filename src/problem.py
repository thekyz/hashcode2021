from typing import List

class Problem(NamedTuple):
    duration: int
    score: int
    street: List[Street] = list()
    cars: List[Car] = list()
