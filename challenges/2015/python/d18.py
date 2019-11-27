'''

Advent of Code - 2015

    --- Day 18: Like a GIF For Your Yard ---

'''

from itertools import product
from copy import deepcopy

rules = {
    '#': lambda grid, neighbors: ('#' if len([(x, y) for (x, y) in neighbors if grid[x][y] == '#']) in [2, 3] else '.'),
    '.': lambda grid, neighbors: ('#' if len([(x, y) for (x, y) in neighbors if grid[x][y] == '#']) == 3 else '.')
}

def memoize(f):
    memo = {}
    def helper(x, y, xmax, ymax):
        if (x, y) not in memo:
            memo[(x, y)] = f(x, y, xmax, ymax)
        return memo[(x, y)]
    return helper

@memoize
def adj(x, y, xmax, ymax):
    return [(x+x1, y+y1) for (x1, y1) in product((-1, 0, 1), (-1, 0, 1)) 
        if (x1 != 0 or y1 != 0) and 0<=x+x1<xmax and 0<=y+y1<ymax]

def animate(grid, xmax, ymax):
    update = deepcopy(grid)
    for y in range(ymax):
        for x in range(xmax):
            update[x][y] = rules[grid[x][y]](grid, adj(x, y, xmax, ymax))

    return update
    
def part1(instructions, xmax=100, ymax=100, steps=100):
    grid = [list(i.strip()) for i in instructions]
    for _ in range(steps):
        grid = animate(grid, xmax, ymax)

    return sum(row.count('#') for row in grid)

def part2(instructions, xmax=100, ymax=100, steps=100):
    grid = [list(i.strip()) for i in instructions]
    grid[0][0] = grid[0][99] = grid[99][0] = grid[99][99] = '#'
    for _ in range(steps):
        grid = animate(grid, xmax, ymax)
        #reset the four corners
        grid[0][0] = grid[0][99] = grid[99][0] = grid[99][99] = '#'

    return sum(row.count('#') for row in grid)

if __name__ == '__main__':
    with open('../input/d18.txt', mode='r') as f:
        _input = f.readlines()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
