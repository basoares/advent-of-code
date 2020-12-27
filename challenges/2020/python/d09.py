'''

Advent of Code - 2020

--- Day 9: Encoding Error  ---

'''

from utils import *

def parse_input(day):
    return day_input(day, int)

def sums(numbers):
    return {n1+n2 for i, n1 in enumerate(numbers) for j, n2 in enumerate(numbers) if i<j and n1!=n2}

def part1(data):
    for n in range(25, len(data)):
        if data[n] not in sums(data[n-25:n]):
            return data[n]

def part12(data):
    for n in range(25, len(data)):
        if not any(x for x in data[n-25:n] if data[n]-x in data[n-24:n]):
            return data[n]

def part2(data, target=556543474):
    for n, i in enumerate(data):
        acc = i
        min_ = i
        max_ = i
        for j in data[n+1:]:
            acc += j
            min_ = min(j, min_)
            max_ = max(j, max_)
            if acc == target:
                return min_ + max_
            elif acc > target:
                break

if __name__ == '__main__':
    data = parse_input('09')

    print(f'Part One: {part1(data)}')
    #print(f'Part One: {part12(data)}')
    print(f'Part Two: {part2(data)}')
