'''

Advent of Code - 2024

--- Day 1: Historian Hysteria --- 

'''

from utils import *

def parse_input(day):
    return day_input(day, parser=integers)


@profiler
def part1(data):
    l, r = zip(*data)
    return sum(abs(x-y) for x, y in zip(sorted(l), sorted(r)))


@profiler
def part2(data):
    l, r = zip(*data)
    #return sum(x*len([n for n in r if n == x]) for x in l)
    return sum(x * r.count(x) for x in l)

    
if __name__=='__main__':
    data = parse_input('01')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')