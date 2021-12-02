'''

Advent of Code - 2021

--- Day 1: Sonar Sweep ---

'''

from utils import day_input

def parse_input(day):
    return day_input(day, int)

def part1(data):
    return sum(b > a for a, b in zip(data, data[1:]))

def part2(data):
    window = list(zip(data, data[1:], data[2:]))
    return sum(sum(b) > sum(a) for a, b in zip(window, window[1:]))

def part22(data):
    return sum(b > a for a, b in zip(data, data[3:]))

if __name__=='__main__':
    data = parse_input('01')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')