'''

Advent of Code - 2023

--- Day 18: Lavaduct Lagoon ---

'''

from utils import *

def parse_input(day):
    return day_input(day, parser=lambda line: line.split())

@profiler
def part1(data):
    b = x = y = 0
    coords = [(x, y)]

    for d, n, _ in data:
        b += int(n)
        dx, dy = { 'U': (0, -1), 'R': (1, 0), 'D': (0, 1), 'L': (-1, 0) }[d]
        x += dx * int(n)
        y += dy * int(n)
        coords.append((x, y))

    # https://en.wikipedia.org/wiki/Shoelace_formula#Other_formulas
    area = abs(sum(coords[i][0] * (coords[(i+1)%len(coords)][1] - coords[i-1][1] ) for i in range(len(coords))) // 2)
    # https://en.wikipedia.org/wiki/Pick%27s_theorem 
    # Area = i + (b/2) - 1, where b is the number of points (vertices and points along the sides)
    i = abs((b//2) - 1 - area)
    
    return i + b

@profiler
def part2(data):
    b = x = y = 0
    coords = [(x, y)]

    for _, _, code in data:
        d, n = { '0': 'R', '1': 'D', '2': 'L', '3': 'U'}[code[-2]], code[2:7]
        b += int(n, 16)
        dx, dy = { 'U': (0, -1), 'R': (1, 0), 'D': (0, 1), 'L': (-1, 0) }[d]
        x += dx * int(n, 16)
        y += dy * int(n, 16)
        coords.append((x, y))

    area = abs(sum(coords[i][0] * (coords[(i+1)%len(coords)][1] - coords[i-1][1] ) for i in range(len(coords))) // 2)
    i = abs((b//2) - 1 - area)
    
    return i + b

if __name__=='__main__':
    data = parse_input('18')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')