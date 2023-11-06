'''

Advent of Code - 2017

--- Day 2: Corruption Checksum ---

'''

from utils import *

def parse_input(day):
    return day_input(day, parser=integers)

@profiler
def part1(data):
    return sum(max(row)-min(row) for row in data)

@profiler
def part2(data):
    return sum(b // a for row in data for a in row for b in row if b > a and b % a == 0)

if __name__=='__main__':
    data = parse_input('02')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')