'''

Advent of Code - 2024

--- Day 3: Mull it Over --- 

'''

from utils import *

def parse_input(day):
    return day_input(day, delimiter='\n\n') # delimiter = '\n\n' will cause all lines to be concatenated


def parse_instructions(line):
    return [tuple(map(int, p)) for p in re.findall(r'mul\((\d+),(\d+)\)', line)]


@profiler
def part1(data):
    instructions = parse_instructions(data[0])
    return sum(a*b for a, b in instructions)


@profiler
def part2(data):
    parts = data[0].split('do()')
    res = 0
    for part in parts:
        before, *after = part.split("don't()")
        res += sum(a*b for a, b in parse_instructions(before))

    return res 

if __name__=='__main__':
    data = parse_input('03')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')