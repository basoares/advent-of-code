'''

Advent of Code - 2015

--- Day 1: Not Quite Lisp ---

'''

from utils import *

def parse_input(day):
     return day_input(day)[0]

@profiler
def part1(instructions):
    return sum({'(': 1, ')': -1}[i] for i in instructions)

@profiler
def part2(instructions):
    return list(accumulate({'(': 1, ')': -1}[i] for i in instructions)).index(-1) + 1

if __name__ == '__main__':
        data = parse_input('01')

        print('Part One: {}'.format(part1(data)))
        print('Part Two: {}'.format(part2(data)))
