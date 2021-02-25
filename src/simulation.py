#!/usr/bin/env python3
import sys
from problem import Problem
from street import Street
from car import Car
from pathlib import Path
from typing import List, Set, Dict, NamedTuple


def simulation_loop():
    return 0


def score_solution(problem: Problem):
    current_time = 0
    score = 0
    while current_time < problem.duration:
        loop_score = simulation_loop()
        score += loop_score
        current_time += 1

    return score


def main(file_to_read: Path, output_folder: Path):
    """
    Main function of program
    """
    print(f"reading {file_to_read}")
    street_dict: Dict[str, Street] = {}
    car_list: List[Car] = []
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
        car_info: List[Car]
        for i in range(amt_cars):
            split_line: List[str] = ftr.readline().strip().split(" ")
            # The car stas at the end of the first street
            amt_streets_for_car: int = int(split_line[0])
            street_names: List[str] = split_line[1:]
            car_list.append(Car(i, street_names))

    print(street_dict)
    print(car_list)

    problem = Problem(duration=6, score=1000)#, street=streets, cars=cars)
    print('+++++ start simulation')
    #solution: Solution = Solution()
    score = score_solution(problem)
    print(f'total score: {score}')
    print('+++++ end simulation')

    #solution: Solution = calculate_solution()

    #output_file = output_folder.joinpath(file_to_read.stem + '_output.txt') 
    #print(f"writing to: {output_file}")
    #if not output_folder.exists():
    #    output_folder.mkdir(parents=True)
    #    print(f"Created output folder {output_folder}")

    #with output_file.open('w') as ftw:
    #    ftw.write('someline')
    #    ftw.write('someline 2\n')
    #    ftw.write('someline 3')
    #    ftw.write('\n')
    #    ftw.write('end\n')

if __name__ == '__main__':
    current_file = Path(sys.argv[1])
    output_folder = Path(sys.argv[2])
    main(current_file, output_folder)
