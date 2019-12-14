'''

Advent of Code - 2019

--- Day 9: Sensor Boost ---

'''

from utils import *
from intcode import IntcodeRunner, HaltExecution

def parse_input(day):
    return day_input(day, integers)[0]

def part1(program):
    runner = IntcodeRunner(program)
    run = runner.run()

    while True: 
        try:
            next(run)
            run.send(1)
        except HaltExecution:
            break

    return runner.output

def part2(program):
    runner = IntcodeRunner(program)
    run = runner.run()

    while True: 
        try:
            next(run)
            run.send(2)
        except HaltExecution:
            break

    return runner.output

if __name__ == '__main__':
    data = parse_input('09')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')

