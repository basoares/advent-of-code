'''

Advent of Code - 2021

--- Day 5: Hydrothermal Venture ---

'''

from utils import *

def parse_input(day):
    parser = lambda line: re.findall(r'\d+', line)
    return day_input(day, parser)


def slope_intersect(x1, y1, x2, y2):
    slope = None
    if x1 != x2:
        slope = (y2-y1)//(x2-x1)

    intersect = x1
    if slope is not None:
        intersect = y1 - slope * x1
    
    return slope, intersect

@profiler
def part1(data):
    vents = defaultdict(lambda: 0)
    for x1, y1, x2, y2 in [map(int, d) for d in data]:
        if y1 == y2: #horizontal
            for x in range(min(x1, x2), max(x1, x2)+1):
                vents[(x, y1)] += 1
        elif x1 == x2: #vertical
            for y in range(min(y1, y2), max(y1, y2)+1):
                vents[(x1, y)] += 1
        else:
            pass

    return len([k for k, v in vents.items() if v > 1])

@profiler
def part2(data):
    vents = defaultdict(lambda : 0)
    for x1, y1, x2, y2 in [map(int, d) for d in data]:
        if y1 == y2: #horizontal
            for x in range(min(x1, x2), max(x1, x2)+1):
                vents[(x, y1)] += 1
        elif x1 == x2: #vertical
            for y in range(min(y1, y2), max(y1, y2)+1):
                vents[(x1, y)] += 1
        else:
            m, b = slope_intersect(x1, y1, x2, y2)
            
            assert m is not None
            assert b is not None
            for x in range(min(x1, x2), max(x1, x2)+1):
                y = x*m + b
                vents[(x, y)] += 1

    return len([k for k, v in vents.items() if v > 1])


@profiler
def part2(data):
    def sign(a, b):
        return 0 if a==b else 1 if a<b else -1

    vents = defaultdict(lambda : 0)
    for x1, y1, x2, y2 in [map(int, d) for d in data]:
        dx = sign(x1, x2)
        dy = sign(y1, y2)

        vents[(x1, y1)] += 1
        while x1!=x2 or y1!=y2:
            x1 += dx
            y1 += dy
            vents[(x1, y1)] += 1

    return len([k for k,v in vents.items() if v > 1])

if __name__=='__main__':
    data = parse_input('05')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')