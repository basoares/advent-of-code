'''

Advent of Code - 2023

--- Day 10: Pipe Maze ---

'''

from utils import *

def parse_input(day):
    return day_input(day)

directions = {'|': [(0, -1), (0, 1)],
              '-': [(-1, 0), (1, 0)],
              'L': [(0, -1), (1, 0)],
              'J': [(-1, 0), (0, -1)],
              '7': [(-1, 0), (0, 1)],
              'F': [(0, 1), (1, 0)],
              '.': []
             }

@profiler
def part1(data):
    S = [(x, y) for y, line in enumerate(data) for x, c in enumerate(line) if c == 'S'][0]
    for (x, y) in neighbors4(S):
        g = data[y][x]
        for (x2, y2) in directions[g]:
            if (x+x2, y+y2) == S:
                pos = (x, y)
                break
    seen = set([S, pos])

    steps = 1
    while True:
        steps += 1
        x, y = pos
        g = data[y][x]
        for d in directions[g]:
            if (x+d[0], y+d[1]) not in seen:
                pos = (x+d[0], y+d[1])
                seen.add(pos)
                break
        else: #both connected positions have been seen, i.e., the loop is closed
            return steps//2

@profiler
def part2(data):
    return None

if __name__=='__main__':
    data = parse_input('10')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')