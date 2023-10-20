'''

Advent of Code - 2022

--- Day 9: Rope Bridge ---

'''

from utils import *

def parse_input(day):
    return day_input(day, parser = lambda line: line.split())
    
motions = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}

def sign(n):
    return 0 if n == 0 else +1 if n > 0 else -1

def updateTail(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]

    if abs(dx) <= 1 and abs(dy) <= 1:
        return tail
    else:
        return (tail[0] + sign(dx), tail[1] + sign(dy))

@profiler
def part1(data):
    head = (0, 0)
    tail = (0, 0)
    seen = { tail }
    for d, steps in data:
        for _ in range(int(steps)):
            head = (head[0] + motions[d][0], head[1] + motions[d][1])
            tail = updateTail(head, tail)
            seen.add(tail)

    return len(seen)

@profiler
def part2(data):
    knots = [(0, 0)] * 10
    seen = { (0, 0) }
    for d, steps in data:
        for _ in range(int(steps)):
            knots[0] = (knots[0][0] + motions[d][0], knots[0][1] + motions[d][1])
            for k in range(1, 10):
                knots[k] = updateTail(knots[k-1], knots[k])
            seen.add(knots[-1])

    return len(seen)

if __name__=='__main__':
    data = parse_input('09')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')