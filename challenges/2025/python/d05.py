'''

Advent of Code - 2025

--- Day 5: Cafeteria --- 

'''

from utils import *

def parse_input(day):
    rs, ings = day_input(day, delimiter='\n\n')  

    ranges = []
    for line in rs.splitlines():
        ranges.append(tuple(map(int, re.findall(r'\d+', line))))

    ingredients = []
    for i in ings.splitlines():
        ingredients.append(int(i))

    return ranges, ingredients

@profiler
def part1(data):
    ranges, ingredients = data
    total = 0
    for ing in ingredients:
        for r in ranges:
            if r[0] <= ing <= r[1]:
                total += 1
                break
    return total

@profiler
def part2(data):
    ranges, _ = data

    ranges = sorted(ranges, key=lambda x: x[0])
    overlap = True
    merged = [ranges.pop(0)]
    while overlap and ranges:
        overlap = False
        start, end = ranges.pop(0)
        for (ms, me) in merged:
            if start <= me and end >= ms: # overlap
                merged.remove((ms, me))
                merged.append((min(start, ms), max(end, me)))
                overlap = True
                break
        if not overlap:
            merged.append((start, end))
            overlap = True

    return sum(e - s + 1 for (s, e) in merged)

    
if __name__=='__main__':
    data = parse_input('05')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')