'''

Advent of Code - 2019

--- Day 1: The Tyranny of the Rocket Equation ---

'''

from utils import *

def parse_input(day):
    return list(day_input(day, int))

def part1(data):
    return sum(mass//3-2 for mass in data)

def part2(data):
    total = 0
    for mass in data:
        module = mass//3-2
        total += module
        fuel = module//3-2
        while fuel>0:
            total += fuel
            fuel = fuel//3-2

    return total

if __name__ == '__main__':
    data = parse_input('01')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
