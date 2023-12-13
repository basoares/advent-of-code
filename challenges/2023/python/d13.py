'''

Advent of Code - 2023

--- Day 13: Point of Incidence ---

'''

from utils import *

def parse_input(day):
    return day_input(day, delimiter='\n\n')

def reflection(pattern,max_diff=0):
    for i in range(len(pattern)-1):
        diff = sum(1 if a != b else 0 for a, b in zip(pattern[i], pattern[i+1]))
        if diff <= max_diff:
            y1 = i - 1
            y2 = i + 2
            while y1 >= 0 and y2 < len(pattern):
                diff += sum(1 if a != b else 0 for a, b in zip(pattern[y1], pattern[y2]))
                if diff <= max_diff:
                    y1 -= 1
                    y2 += 1
                else:
                    break # mismatch
            else: #did not end via the break, meaning we reached one of the edges
                if diff == max_diff:
                    return i+1
    return 0

@profiler
def part1(data):
    ans = 0
    for pattern in data:
        # horizontal
        score = reflection(pattern.split())
        ans += score*100

        # vertical
        transposed = list(zip(*pattern.split()))
        score = reflection(transposed)
        ans += score
    return ans

@profiler
def part2(data):
    ans = 0
    for pattern in data:
        # horizontal
        score = reflection(pattern.split(), 1)
        ans += score*100

        # vertical
        transposed = list(zip(*pattern.split()))
        score = reflection(transposed, 1)
        ans += score
    return ans

if __name__=='__main__':
    data = parse_input('13')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')