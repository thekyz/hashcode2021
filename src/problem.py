from typing import List, NamedTuple, Dict, Optional, Deque
from collections import deque

class Problem():
    pass

class Car():
    id: int
    street_names: List[str]
    problem: Problem

    time_left_on_street: int
    current_street_index: int

    done: bool

    def __init__(self, id, street_names, problem):
        self.id = id
        self.street_names = street_names
        self.streets_len = len(self.street_names)
        self.problem = problem

        self.time_left_on_street = 0
        self.current_street_index = 0

        self.current_street = problem.streets[self.street_names[self.current_street_index]]

        self.done = False

    def init(self, problem):
        print(f'car {self.id} entering street {self.current_street.name}')
        self.current_street.enter(self)

    def update(self):
        if self.done:
            return 0

        if not self.time_left_on_street:
            if self.current_street.can_leave(self):
                # leave current street
                print(f'car {self.id} leaving street {self.current_street.name}')
                self.time_left_on_street = self.current_street.leave(self)

                self.current_street_index += 1
                if self.current_street_index >= self.streets_len:
                    # car is done
                    print(f'car {self.id} done')
                    self.done = True
                    return 1

                self.current_street = self.problem.streets[self.street_names[self.current_street_index]]

                # enter next one
                print(f'car {self.id} entering street {self.current_street.name}')
                self.current_street.enter(self)
        else:
            self.time_left_on_street -= 1

        return 0


class Street():
    name: str
    time_to_cross: int
    start_id: int
    end_id: int

    car_queue: Deque[Car]
    is_green: bool

    def __init__(self, name, time_to_cross, start_id, end_id):
        self.name = name
        self.time_to_cross = time_to_cross
        self.start_id = start_id
        self.end_id = end_id

        self.car_queue = deque()
        self.is_green = False


    def leave(self, car):
        # remove from the right of the dequ
        self.car_queue.pop()

    def enter(self, car):
        # append to the left of the deque
        self.car_queue.appendleft(car)
        return self.time_to_cross

    def can_leave(self, car):
        if self.is_green:
            return True

        return False


class Problem(NamedTuple):
    duration: int
    score: int
    streets: Dict[str, Street] = {}
    cars: List[Car] = list()
