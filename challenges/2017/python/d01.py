'''

Advent of Code - 2017

--- Day 1: Inverse Captcha ---

'''

from utils import *

def parse_input(day):
    return day_input(day)[0]

@profiler
def part1(data):
    captcha = data + data[-1]
    return sum(int(x) for x,y in zip(captcha, captcha[1:]) if x == y )

@profiler
def part2(data):
    n = len(data)
    return sum(int(c) for i, c in enumerate(data) if c == data[(i+(n//2)) % n])

if __name__=='__main__':
    data = parse_input('01')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')