'''

Advent of Code - 2022

--- Day 4: Camp Cleanup ---

'''

from utils import *

def parse_input(day):
    return day_input(day, digits)

@profiler
def part1(data):
    return sum((x2 <= x1 and y1 <= y2) or (x1 <= x2 and y2 <= y1) for x1, y1, x2, y2 in data)

@profiler
def part2(data):
    #(StartA <= EndB) and (EndA >= StartB)
    return sum(x1 <= y2 and y1 >= x2 for x1, y1, x2, y2 in data)

if __name__=='__main__':
    data = parse_input('04')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')