'''

Advent of Code - 2019

    --- Day 4: Secure Container ---

'''

from utils import *

def parse_input(day):
    parser = lambda line : line.split('-')
    return day_input(day, parser)[0]

def is_increasing(n):
    digits = str(n)
    return all(x <= y for x, y in zip(digits, digits[1:]))

def has_two_of_the_same(n):
    digits = str(n)
    return any(x == y for x, y in zip(digits, digits[1:]))

def has_only_two_of_the_same(n):
    digits = str(n)
    return any(d*2 in digits and d*3 not in digits for d in '0123456789')

def part1(password_range):
    LO, HI = password_range

    return sum(is_increasing(n) and has_two_of_the_same(n) for n in range(int(LO), int(HI)+1))

def part2(password_range):
    LO, HI = password_range

    return sum(is_increasing(n) and has_only_two_of_the_same(n) for n in range(int(LO), int(HI)+1))
        
if __name__ == '__main__':
    data = parse_input('04')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
