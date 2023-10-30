'''

Advent of Code - 2022

--- Day 14: Regolith Reservoir ---

'''

from utils import *

def parse_input(day):
    raw = day_input(day)
    return [list(map(integers, line.split(' -> '))) for line in raw]


@profiler
def part1(scan, start=(500, 0)):
    grid = defaultdict(lambda: '.')  # default to 'air'
    for line in scan:
        for (x1, y1), (x2, y2) in zip(line, line[1:]):
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    grid[(x, y)] = '#'

    max_y = max(y for (_, y) in grid)
    dirs = [(0, 1), (-1, 1), (1, 1)]
        
    for grains in count(1):
        pos = start
        rest = False
        while not rest:
            rest = True
            for dx, dy in dirs:
                new_pos = (pos[0] + dx, pos[1] + dy)
                if new_pos not in grid:
                    if new_pos[1] > max_y:
                        return grains - 1

                    pos = new_pos
                    rest = False
                    break
                    
            if rest:
                grid[pos] = 'o'


@profiler
def part2(scan, start=(500, 0)):
    grid = defaultdict(lambda: '.')  # default to 'air'
    for line in scan:
        for (x1, y1), (x2, y2) in zip(line, line[1:]):
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    grid[(x, y)] = '#'

    max_y = max(y for (_, y) in grid) + 2
    for x in range(-1000, 1000):
        grid[(x, max_y)] = '#'

    dirs = [(0, 1), (-1, 1), (1, 1)]
        
    for grains in count(1):
        pos = start
        rest = False
        while not rest:
            rest = True
            for dx, dy in dirs:
                new_pos = (pos[0] + dx, pos[1] + dy)
                if new_pos not in grid:
                    pos = new_pos
                    rest = False
                    break
                    
            if rest:
                if pos == start:
                    return grains
                grid[pos] = 'o'


if __name__=='__main__':
    data = parse_input('14')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')