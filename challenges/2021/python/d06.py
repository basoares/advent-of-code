'''

Advent of Code - 2021

--- Day 6: Lanternfish ---

'''

from utils import *

def parse_input(day):
    parser = lambda line: re.findall(r'\d+', line)
    return day_input(day, parser)

def simulate_growth(lanternfish, days):
    counts = Counter(lanternfish)
    for _ in range(days):
        counts_zero = counts[0]
        for i in range(8):
            counts[i] = counts[i+1]
        counts[8] = counts_zero
        counts[6] += counts_zero 

    return counts

@profiler
def part1(data):
    lanternfish = [int(d) for d in data[0]]
    
    counts = simulate_growth(lanternfish, 80)
    return sum(counts.values())

@profiler
def part2(data):
    lanternfish = [int(d) for d in data[0]]

    counts = simulate_growth(lanternfish, 256)
    return sum(counts.values())

if __name__=='__main__':
    data = parse_input('06')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')