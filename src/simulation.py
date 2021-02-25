#!/usr/bin/env python3
import sys
import random
from problem import Car, Street, Problem
from solution import Solution, Intersection
from pathlib import Path
from typing import List, Set, Dict, NamedTuple


def simulation_loop(current_time: int, problem: Problem, solution: Solution):
    for intersection in solution.intersections:
        intersection.green_light(problem, current_time)

    loop_score = 0

    for car in problem.cars:
        if car.update():
            loop_score += problem.score + (problem.duration - current_time)

    return loop_score


def score_solution(problem: Problem, solution: Solution):
    current_time = 0
    score = 0

    for intersection in solution.intersections:
        intersection.init(problem)

    for car in problem.cars:
        car.init(problem)

    print('------- init done')

    while current_time <= problem.duration:
        print(f'======= loop {current_time}')
        loop_score = simulation_loop(current_time, problem, solution)
        score += loop_score
        current_time += 1

    return score

INTERSECTION_RATE = .5
ACTIVE_STREET_RATE = 1.0
AVERAGE_GREEN_TIME = 3
VARIANCE_GREEN_TIME = 2


def generate_solution(all_intersections):
    result = []
    for intersection in all_intersections:
        if not intersection.streets:
            continue

        if random.random() > INTERSECTION_RATE:
            streets = [random.choice(intersection.streets)]
        else:
            streets = []
            for street in intersection.streets:
                if random.random() < ACTIVE_STREET_RATE:
                    streets.append(street)

        if not streets:
            streets = [random.choice(intersection.streets)]

        intersection_result = []
        for street, _ in streets:
            street_time = int(max(1, AVERAGE_GREEN_TIME + random.random() * VARIANCE_GREEN_TIME))
            intersection_result.append((street, street_time))

        result.append(Intersection(intersection.id, intersection_result))

    return result


def main(file_to_read: Path, output_folder: Path):
    """
    Main function of program
    """
    print()
    print()
    print()
    print()
    print()
    print(f"reading {file_to_read}")
    street_dict: Dict[str, Street] = {}
    car_list: List[Car] = []
    problem = Problem(duration=6, score=1000, streets=street_dict, cars=car_list)
    with file_to_read.open() as ftr:
        duration: int
        amt_intersections: int
        amt_streets: int
        amt_cars: int
        bonus_points: int
        duration, amt_intersections, amt_streets, amt_cars, bonus_points = map(int, ftr.readline().strip().split(" "))
        for i in range(amt_streets):
            split_line: List[str] = ftr.readline().strip().split(" ")
            start_intersection_id: int
            end_intersection_id: int
            start_intersection_id, end_intersection_id = map(int, split_line[:2])
            street_name = split_line[2]
            street_time = int(split_line[3])
            street_dict[street_name] = Street(street_name, start_intersection_id, end_intersection_id, street_time)

        # paths of the cars
        for i in range(amt_cars):
            split_line: List[str] = ftr.readline().strip().split(" ")
            # The car stas at the end of the first street
            amt_streets_for_car: int = int(split_line[0])
            street_names: List[str] = split_line[1:]
            car_list.append(Car(i, street_names, problem))

    print(street_dict)
    print(car_list)

    print('+++++ start simulation')

    all_intersections = problem.get_intersections(amt_intersections)
    print(all_intersections)

    solution = Solution(generate_solution(all_intersections))
    score = score_solution(problem, solution)
    print('+++++ end simulation')
    print()
    print(f'total score: {score}')
    print()

    output_file = output_folder.joinpath(file_to_read.stem + '_output.txt') 
    solution.write_output(output_file)

if __name__ == '__main__':
    current_file = Path(sys.argv[1])
    output_folder = Path(sys.argv[2])
    main(current_file, output_folder)
