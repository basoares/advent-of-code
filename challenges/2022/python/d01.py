'''

Advent of Code - 2022

--- Day 1: Calorie Counting ---

'''

from utils import *

def parse_input(day):
    return [integers(elf) for elf in day_input(day, delimiter='\n\n')]

@profiler
def part1(data):
    return max(sum(calories) for calories in data)

@profiler
def part2(data):
    return sum(sorted((sum(calories) for calories in data), reverse=True)[:3])

if __name__=='__main__':
    data = parse_input('01')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')