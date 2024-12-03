'''

Advent of Code - 2024

--- Day 2: Red-Nosed Reports --- 

'''

from utils import *

def parse_input(day):
    return day_input(day, parser=integers)


def is_valid(report):
    diffs = [b-a for a, b in zip(report, report[1:])]
    return all(d in [1,2,3] for d in diffs) or all(d in [-1, -2, -3] for d in diffs)

@profiler
def part1(data):
    return sum(1 for report in data if is_valid(report))

@profiler
def part2(data):
    res = 0
    for report in data:
        if is_valid(report):
            res += 1
        else:
            for n in range(len(report)):
                if is_valid(report[:n] + report[n+1:]):
                    res += 1
                    break
    return res
    
if __name__=='__main__':
    data = parse_input('02')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')