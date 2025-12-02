'''

Advent of Code - 2025

--- Day 1: Secret Entrance --- 

'''

from utils import *

def parse_input(day):
    parser = lambda x: (x[0], int(x[1:]))
    return day_input(day, parser)


dirs = {'L': -1, 'R': 1}


@profiler
def part1(data, pos=50, N=100):
    res = 0
    for dir, rotation in data:
        pos = (pos + rotation * dirs[dir]) % N
        if pos == 0:
            res += 1
    return res


@profiler
def part2(data, pos=50, N=100):
    res = 0
    for dir, rotation in data:
        turns, units = divmod(rotation, N)
        res += turns
        new_pos = pos + dirs[dir]*units
        if new_pos >= N or pos and new_pos <= 0:    # if completed a loop (new position >= N) or cross from positive to negative
            res += 1
        pos = new_pos % N
    return res


if __name__=='__main__':
    data = parse_input('01')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')