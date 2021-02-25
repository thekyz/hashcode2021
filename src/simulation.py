#!/usr/bin/env python3

from problem import Problem
from street import Street
from car import Car

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

if __name__ == '__main__':
    #streets = [
    #    Street(name='rue-de-londres', start_id=2, end_id=0, time_to_cross=1),
    #    Street(name='rue-d-amsterdam', start_id=0, end_id=1, time_to_cross=1),
    #    Street(name='rue-d-athenes', start_id=3, end_id=1, time_to_cross=1),
    #    Street(name='rue-de-rome', start_id=2, end_id=3, time_to_cross=2),
    #    Street(name='rue-de-moscou', start_id=1, end_id=2, time_to_cross=3),
    #]

    #cars = [
    #    Car(4, [streets[0], streets[1], streets[4], streets[3]]),
    #    Car(3, [streets[2], streets[4], streets[0]]),
    #]

    problem = Problem(duration=6, score=1000)#, street=streets, cars=cars)
    print('+++++ start simulation')
    #solution: Solution = Solution()
    score = score_solution(problem)
    print(f'total score: {score}')
    print('+++++ end simulation')
