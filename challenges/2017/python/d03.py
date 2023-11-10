'''

Advent of Code - 2017

--- Day 3: Spiral Memory ---

'''

from utils import *

def parse_input(day):
    return int(day_input(day)[0])

def square_spiral():
    x = y = s = 0
    yield (x, y)
    while True:
        for (dx, dy) in ((0, -1), (1, 0), (0, 1), (-1, 0)):
            if dy:
                s += 1
            for _ in range(s):
                x += dx
                y += dy
                yield (x, y)

@profiler
def part1(data):
    #n = list(islice(square_spiral(), data))
    #return manhattan_distance((0, 0), n[data-1])
    n = next(islice(square_spiral(), data-1, None))
    return manhattan_distance((0, 0), n)

@profiler
def part2(data):
    sums = defaultdict(int)
    for n in square_spiral():
        sums[n] = sum(sums[p] for p in neighbors8(n) if p in sums) or 1

        if sums[n] > data:
            return sums[n]


if __name__=='__main__':
    data = parse_input('03')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')