'''

Advent of Code - 2022

--- Day 6: Tuning Trouble ---

'''

from utils import *

def parse_input(day):
    return day_input(day)[0]

@profiler
def part1(data):
    for i in range(3, len(data)):
        if len(set(data[i-4:i])) == 4:
            return i

@profiler
def part2(data):
    for i in range(13, len(data)):
        if len(set(data[i-14:i])) == 14:
            return i

if __name__=='__main__':
    data = parse_input('06')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')