from typing import List, NamedTuple, Dict, Optional

class Problem():
    pass

class Car():
    id: int
    street_names: List[str]
    problem: Problem

    time_left_on_street: int
    current_street_index: int

    def __init__(self, id, street_names, problem):
        self.id = id
        self.street_names = street_names
        self.problem = problem

        self.time_left_on_street = 0
        self.current_street_index = 0

        self.current_street = problem.streets[self.street_names[self.current_street_index]]

    def update(self):
        if not self.time_left_on_street:
            if self.current_street.can_leave(self):
                # leave current street
                self.time_left_on_street = self.current_street.leave(self)

                self.current_street_index += 1
                self.current_street = self.problem.streets[self.street_names[self.current_street_index]]
                print(f'car {self.id} entering street index {self.current_street.name}')

                # enter next one
                self.current_street.enter(self)
        else:
            self.time_left_on_street -= 1

        return 0


class Street():
    name: str
    time_to_cross: int
    start_id: int
    end_id: int

    car_queue: List[Car]
    is_green: bool

    def __init__(self, name, time_to_cross, start_id, end_id):
        self.name = name
        self.time_to_cross = time_to_cross
        self.start_id = start_id
        self.end_id = end_id

        self.car_queue = []
        self.is_green = False


    def leave(self, car):
        self.car_queue.pop(0)

    def enter(self, car):
        self.car_queue.append(car)
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
