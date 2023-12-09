'''

Advent of Code - 2023

--- Day 9: Mirage Maintenance ---

'''

from utils import *

def parse_input(day):
    return day_input(day, integers)

def extrapolate(sequence):
    if any(n for n in sequence):
        return [sequence[-1]] + extrapolate([sequence[i]-sequence[i-1] for i in range(1, len(sequence))])
    else:
        return [sequence[-1]]

@profiler
def part1(data):
    return sum(sum(extrapolate(sequence)) for sequence in data)

@profiler
def part2(data):
    return sum(sum(extrapolate(list(reversed(sequence)))) for sequence in data)

if __name__=='__main__':
    data = parse_input('09')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')