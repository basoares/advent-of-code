'''

Advent of Code - 2021

--- Day 2: Dive! ---

'''

from utils import *

def parse_input(day):
    parser = lambda line: re.search(r'(\w+) (\d+)', line).groups()
    return day_input(day, parser)

def part1(data):
    horizontal = 0
    depth = 0
    for command, n in data:
        if command == 'forward':
            horizontal += int(n)
        else:
            depth += int(n) if command == 'down' else -1 * int(n)
    return horizontal * depth

def part2(data):
    horizontal = 0
    aim = 0
    depth = 0
    for command, n in data:
        if command == 'forward':
            horizontal += int(n)
            depth += aim * int(n)
        else:
            aim += int(n) if command == 'down' else -1 * int(n)

    return horizontal * depth

if __name__=='__main__':
    data = parse_input('02')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')