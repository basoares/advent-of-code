'''

Advent of Code - 2016

--- Day 6: Signals and Noise ---

'''

from utils import *

def parse_input(day):
    return day_input(day)

@profiler
def part1(data):
    return ''.join([Counter(msg).most_common()[0][0] for msg in zip(*data)])

@profiler
def part2(data):
    return ''.join([Counter(msg).most_common()[-1][0] for msg in zip(*data)])

if __name__=='__main__':
    data = parse_input('06')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')