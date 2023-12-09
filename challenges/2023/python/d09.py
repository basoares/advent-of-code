'''

Advent of Code - 2023

--- Day 9: Mirage Maintenance ---

'''

from utils import *

def parse_input(day):
    return day_input(day, integers)

@profiler
def part1(data):
    ans = 0
    for seq in data:
        diffs = []
        aux = seq
        while True:
            next_seq = []
            for i in range(1, len(aux)):
                next_seq.append(aux[i] - aux[i-1])
            if any(n for n in next_seq):
                diffs.append(aux[-1])
            else:
                diffs.append(aux[-1])
                ans += reduce(lambda x, y: x+y, diffs)
                break
            aux = next_seq
    return ans

@profiler
def part2(data):
    ans = 0
    for seq in data:
        diffs = []
        aux = list(reversed(seq))
        while True:
            next_seq = []
            for i in range(1, len(aux)):
                next_seq.append(aux[i] - aux[i-1])
            if any(n for n in next_seq):
                diffs.append(aux[-1])
            else:
                diffs.append(aux[-1])
                ans += reduce(lambda x, y: x+y, diffs)
                break
            aux = next_seq
    return ans

if __name__=='__main__':
    data = parse_input('09')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')