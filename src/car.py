from typing import List, NamedTuple
from street import Street


class Car(NamedTuple):
    id: int
    street_names: List[str]