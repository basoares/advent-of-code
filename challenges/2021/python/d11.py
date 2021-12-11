'''

Advent of Code - 2021

--- Day 11: Dumbo Octopus ---

'''

from utils import *

def parse_input(day):
    raw = day_input(day)
    grid = {
        (i, j): int(e)
        for i, line in enumerate(raw)
        for j, e in enumerate(line)
    }
    return grid

def flash(o, grid, flashed):
    if o in flashed:
        return 0

    flashed.add(o)
    for x, y in neighbors8(o):
        if (x, y) not in grid or (x, y) in flashed:
            continue

        grid[x, y] += 1
        if grid[x, y] > 9 and (x, y) not in flashed:
            grid[x, y] = 0
            flash((x, y), grid, flashed)

    return 0


def step(grid):
    # increase the energy level of all octopus
    for i, j in grid:
        grid[i, j] += 1
    
    flashed = set()
    for (i, j), o in grid.items():
        if o > 9 and (i, j) not in flashed:
            grid[i, j] = 0 #reset
            flash((i, j), grid, flashed)
            
    return len(flashed)

def show_grid(grid):
    for i in range(10):
        print(''.join(str(grid[i, j]) for j in range(10)))

@profiler
def part1(data):
    grid = data
    flashes = 0
    for _ in range(100):
        flashes += step(grid)

    return flashes

@profiler
def part2(data):
    grid = data
    for s in count(1):
        if step(grid) == len(grid):
            return s

if __name__=='__main__':
    data = parse_input('11')
    print(f'Part One: {part1(data)}')

    # because the status of the grid is changed, we reload the data for part2
    data = parse_input('11')
    print(f'Part Two: {part2(data)}')