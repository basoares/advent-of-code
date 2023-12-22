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
    S = [(x, y) for y, line in enumerate(data) for x, c in enumerate(line) if c == 'S'][0]
    for (x, y) in neighbors4(S):
        g = data[y][x]
        for (x2, y2) in directions[g]:
            if (x+x2, y+y2) == S:
                pos = (x, y)
                break
    poly = [S, pos]

    done = False
    steps = 1
    while not done:
        steps += 1
        x, y = pos
        g = data[y][x]
        for d in directions[g]:
            if (x+d[0], y+d[1]) not in poly:
                pos = (x+d[0], y+d[1])
                poly.append(pos)
                break
        else:
            done = True

    ans = 0
    for y, row in enumerate(data):
        for x, p in enumerate(row):
            if is_in_polygon((x, y), poly):
                ans += 1

    return ans

def is_in_polygon(point, poly):
    #even-odd rule: https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule
    x, y = point
    num = len(poly)
    j = num - 1
    c = False
    for i in range(num):
        if (x == poly[i][0]) and (y == poly[i][1]):
            # point is a corner
            return False
        if (poly[i][1] > y) != (poly[j][1] > y):
            slope = (x - poly[i][0]) * (poly[j][1] - poly[i][1]) - (
                poly[j][0] - poly[i][0]
            ) * (y - poly[i][1])
            if slope == 0:
                # point is on boundary
                return False
            if (slope < 0) != (poly[j][1] < poly[i][1]):
                c = not c
        j = i
    return c

if __name__=='__main__':
    data = parse_input('10')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')