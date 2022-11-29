'''

Advent of Code - 2016

--- Day 3: Squares with three sides ---

'''

from utils import *

def parse_input(day):
    return day_input(day, integers)

def is_triangle(a, b, c):
    return 1 if a + b > c else 0

@profiler
def part1(data):
    # https://en.wikipedia.org/wiki/Triangle_inequality
    return sum(is_triangle(*sorted(tri)) for tri in data)

@profiler
def part2(data):
    ans = 0
    for i in range(0, len(data), 3):
        ans += sum(is_triangle(*sorted(tri)) for tri in zip(*data[i:i+3]))

    return ans

if __name__=='__main__':
    data = parse_input('03')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')