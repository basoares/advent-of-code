'''

Advent of Code - 2023

--- Day 11: Cosmic Expansion ---

'''

from utils import *

def parse_input(day):
    return day_input(day)

def expand(grid, offset=1):
    transposed = list(zip(*grid))
    expanded = defaultdict()

    y = 0
    for row in grid:
        if '#' not in row: # if no galaxy in this row, increment the y value of the coordinate 
            y += offset
        x = 0
        for i, c in enumerate(row):
            if '#' not in transposed[i]: # if no galaxy in this column, increment the x value of the coordinate
                x += offset
            if c == '#':
                expanded[(x, y)] = '#'
            x += 1
        y += 1
    return expanded

@profiler
def part1(data):
    expanded_universe = expand(data)
    return sum(manhattan_distance(g1, g2) for (g1, g2) in combinations(expanded_universe, 2))

@profiler
def part2(data):
    expanded_universe = expand(data, 1_000_000 - 1)
    return sum(manhattan_distance(g1, g2) for (g1, g2) in combinations(expanded_universe, 2))

if __name__=='__main__':
    data = parse_input('11')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')