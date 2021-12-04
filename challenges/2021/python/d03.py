'''

Advent of Code - 2021

--- Day 3: Dive! ---

'''

from utils import *

def parse_input(day):
    return day_input(day)

@profiler
def part1(data):
    epsilon = ''
    gamma = ''
    cls = list(zip(*data))
    for n in range(len(data[0])):
        x = sum([int(i) for i in cls[n]])

        if x > len(cls[0])//2:
            epsilon += '0'
            gamma += '1'
        else:
            epsilon += '1'
            gamma += '0'
    
    return int(epsilon, 2) * int(gamma, 2)

def calculate_oxygen(numbers, pos=0):
    if len(numbers) == 1:
        return int(numbers[0], 2)

    cols = list(zip(*numbers))
    if sum([int(i) for i in cols[pos]]) >= len(numbers)/2:
        return calculate_oxygen([n for n in numbers if n[pos] == '1'], pos+1)
    else:
        return calculate_oxygen([n for n in numbers if n[pos] == '0'], pos+1)

def calculate_co2(numbers, pos=0):
    if len(numbers) == 1:
        return int(numbers[0], 2)

    cols = list(zip(*numbers))
    if sum([int(i) for i in cols[pos]]) >= len(numbers)/2:
        return calculate_co2([n for n in numbers if n[pos] == '0'], pos+1)
    else:
        return calculate_co2([n for n in numbers if n[pos] == '1'], pos+1)

@profiler
def part2(data):
    return calculate_oxygen(data) * calculate_co2(data)

if __name__=='__main__':
    data = parse_input('03')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')