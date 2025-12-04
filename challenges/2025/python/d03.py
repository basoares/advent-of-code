'''

Advent of Code - 2025

--- Day 3:  --- 

'''

from utils import *

def parse_input(day):
    return day_input(day)


def joltage(bank, N):
    batteries = []
    pos = 0
    for i in range(1, N+1):
        if -(N-i) == 0:
            m = max(bank[pos:])
        else:
            m = max(bank[pos:-(N-i)])
        batteries.append(m)
        pos = bank[pos:].find(m)+1+pos
    return int(''.join(batteries))


@profiler
def part1(data):
    return sum(joltage(bank, 2) for bank in data)


@profiler
def part2(data):
    return sum(joltage(bank, 12) for bank in data)

    
if __name__=='__main__':
    data = parse_input('03')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')