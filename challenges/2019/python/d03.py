'''

Advent of Code - 2019

    --- Day 3: Crossed Wires ---

'''

from utils import *

def parse_input(day):
    parser = lambda line : line.split(',')
    return day_input(day, parser)

DX = dict(zip('UDLR', [0, 0, -1, 1]))
DY = dict(zip('UDLR', [-1, 1, 0, 0]))

def generate_path(moves):
    coords = defaultdict(int)

    #central port has coordinates (0, 0)
    x, y = 0, 0
    total_steps = 0
    for m in moves:
        direction, steps = m[0], int(m[1:])
        assert direction in 'UDLR'
        for _ in range(steps):
            x += DX[direction]
            y += DY[direction]
            total_steps += 1
            if (x, y) not in coords:
                coords[(x, y)] = total_steps

    return coords

def part1(wires):
    coords_a = generate_path(wires[0])
    coords_b = generate_path(wires[1])

    return min(manhattan_distance((0, 0), c) for c in coords_a.keys()&coords_b.keys())

def part2(wires):
    coords_a = generate_path(wires[0])
    coords_b = generate_path(wires[1])

    return min(coords_a[c]+coords_b[c] for c in coords_a.keys()&coords_b.keys())
        
if __name__ == '__main__':
    data = parse_input('03')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
