from typing import List, NamedTuple
from street import Street
from car import Car

class Problem(NamedTuple):
    duration: int
    score: int
    street: List[Street] = list()
    cars: List[Car] = list()

    
    # update data
