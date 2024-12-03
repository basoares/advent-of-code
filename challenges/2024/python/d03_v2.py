'''

Advent of Code - 2024

--- Day 3: Mull it Over --- 

'''

from utils import *

def parse_input(day):
    return day_input(day, delimiter='\n\n', parser=lambda line: re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)) # delimiter = '\n\n' will cause all lines to be concatenated


@profiler
def part1(data):
    instructions = data[0]
    return sum(mul(*integers(i)) for i in instructions if i not in ("do()", "don't()"))


@profiler
def part2(data):
    enabled = True
    res = 0
    for part in data[0]:
        if part == 'do()':
            enabled = True
        elif part == "don't()":
            enabled = False
        else:
            if enabled:
                res += mul(*integers(part))
    return res 

if __name__=='__main__':
    data = parse_input('03')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')