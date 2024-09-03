'''

Advent of Code - 2016

--- Day 7: Internet Protocol Version 7 ---

'''

from utils import *

def parse_input(day):
    def parser(line):
        parts = re.split(r'\[|\]', line)
        return('|'.join(parts[0::2]), '|'.join(parts[1::2]))

    return day_input(day, parser)


@profiler
def part1(data):
    def supports_tls(parts):
        return any(a == d and b == c and a != b for a, b, c, d in [parts[i:i+4] for i in range(len(parts)+1-4)])

    return sum(1 for outside, inside in data if supports_tls(outside) and not supports_tls(inside))


@profiler
def part2(data):
    def supports_ssl(outside, inside):
        return any(a == c and a != b and b+a+b in outside for a, b, c in [inside[i:i+3] for i in range(len(inside)+1-3)])

    return sum(1 for outside, inside in data if supports_ssl(outside, inside))


if __name__=='__main__':
    data = parse_input('07')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')