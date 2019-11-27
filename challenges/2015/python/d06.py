'''

Advent of Code - 2015

    --- Day 6: Probable a Fire Hazard ---

'''

from collections import defaultdict
import re
from itertools import product

def part1(instructions):
    grid = defaultdict(int)

    for i in instructions:
        x1, y1, x2, y2 = [int(c) for c in re.findall(r'\d+', i)]
        for c in product(range(x1, x2+1), range(y1, y2+1)):
            if 'turn on' in i:
                grid[c] = 1
            elif 'turn off' in i:
                grid[c] = 0
            else: #toggle
                grid[c] = 1 - grid[c]

    return sum(grid.values())

def part2(instructions):
    grid = defaultdict(int)

    for i in instructions:
        x1, y1, x2, y2 = [int(c) for c in re.findall(r'\d+', i)]
        for c in product(range(x1, x2+1), range(y1, y2+1)):
            if 'turn on' in i:
                grid[c] += 1
            elif 'turn off' in i:
                grid[c] -= 1 if grid[c] >= 1 else 0
            else: #toggle
                grid[c] += 2

    return sum(grid.values())

if __name__ == '__main__':
    with open('../input/d06.txt', mode='r') as f:
        _input = f.readlines()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
