'''

Advent of Code - 2020

--- Day 1: Report Repair ---

'''

from utils import day_input

def parse_input(day):
    return day_input(day, int)

def part1(data):
    deltas = {2020-n for n in data}
    for n in data:
        if n in deltas:
            return n*(2020-n)

def part2(data):
    deltas = {2020-i-j:(i, j) for i in data for j in data if i!=j}
    for n in data:
        if n in deltas:
            i, j = deltas[n]
            return n*i*j

if __name__ == '__main__':
    data = parse_input('01')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
