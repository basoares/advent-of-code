'''

Advent of Code - 2023

--- Day 1: Trebuchet!? ---

'''

from utils import *

def parse_input(day):
    return day_input(day)

def calibration_value(numbers):
    return int(numbers[0]+numbers[-1])

@profiler
def part1(data):
    return sum(calibration_value(ds) for ds in map(digits, data))

def find_digits(line):
    mapping = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    d = []
    for i, c in enumerate(line):
        if c.isdigit():
            d.append(c)
        else:
            for j, m in enumerate(mapping):
                if line[i:].startswith(m):
                    d.append(str(j+1))
    return d

@profiler
def part2(data):
    return sum(calibration_value(ds) for ds in map(find_digits, data))
    
if __name__=='__main__':
    data = parse_input('01')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')