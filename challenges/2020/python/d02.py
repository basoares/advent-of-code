'''

Advent of Code - 2020

--- Day 2: Password Philosophy ---

'''

from utils import *

def parse_input(day):
    parser = lambda line: re.search(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
    return day_input(day, parser)

def part1(data):
    return sum(int(lo) <= pwd.count(ch) <= int(hi) for lo, hi, ch, pwd in data)

def part2(data):
    return sum([pwd[int(lo)-1], pwd[int(hi)-1]].count(ch) == 1 for lo, hi, ch, pwd in data)

if __name__ == '__main__':
    data = parse_input('02')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
