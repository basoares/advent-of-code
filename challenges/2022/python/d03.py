'''

Advent of Code - 2022

--- Day 3: Rucksack Reorganization ---

'''

from utils import *

def parse_input(day):
    return day_input(day)

def priority(item):
    #return ord(item) - ord('a') + 1 if item == item.lower() else ord(item) - ord('A') + 27
    return string.ascii_letters.index(item) + 1

@profiler
def part1(data):
    common = []
    for r in data:
        a, b = r[:len(r)//2], r[len(r)//2:]
        assert len(a) == len(b)

        common.append(set(a).intersection(b).pop())

    return sum(priority(item) for item in common)

@profiler
def part2(data):
    common = []
    for i in range(0, len(data), 3):
        common.append(set.intersection(*map(set, data[i:i+3])).pop())

    return sum(priority(item) for item in common)

if __name__=='__main__':
    data = parse_input('03')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')