'''

Advent of Code - 2016

--- Day 1: No Time for a Taxicab ---

'''

from utils import *

def parse_input(day):
    return day_input(day, delimiter=',')

def update_dir(current, turn):
    x, y = current
    # 2d vector (x, y) rotated clockwise by 90 degrees is just (y, -x). Similarly for counterclockwise.
    return (y, -x) if turn == 'R' else (-y, x)

@profiler
def part1(data):
    x, y = 0, 0
    dir = (1, 0)
    for d in data:
        turn, blocks = d[0], int(d[1:])
        if turn in 'LR':
            dir = update_dir(dir, turn)
            x += dir[0] * blocks
            y += dir[1] * blocks
        else:
            raise ValueError(f'Invalid instruction: {(turn, blocks)}')

    return manhattan_distance((0, 0), (x, y))

@profiler
def part2(data):
    seen = set()
    x, y = 0, 0
    dir = (1, 0)
    for d in data:
        turn, blocks = d[0], int(d[1:])
        if turn in 'LR':
            dir = update_dir(dir, turn)
            for _ in range(blocks):
                x += dir[0]
                y += dir[1]
                if (x, y) in seen:
                    return manhattan_distance((0, 0), (x, y))
                seen.add((x, y))
        else:
            raise ValueError(f'Invalid instruction: {(turn, blocks)}')

if __name__=='__main__':
    data = parse_input('01')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')