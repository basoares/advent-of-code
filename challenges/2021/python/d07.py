'''

Advent of Code - 2021

--- Day 7: The Treachery of Whales ---

'''

from utils import *

def parse_input(day):
    parser = lambda line: re.findall(r'\d+', line)
    return day_input(day, parser)

@profiler
def part1(data):
    crabs = map(int, data[0])
    positions = Counter(crabs)

    min_fuel = 1e9
    for p in positions:
        cost = sum(positions[other_pos] * abs(p-other_pos) for other_pos in positions if other_pos  != p)
        if min_fuel > cost:
            min_fuel = cost

    return min_fuel

@profiler
def part12(data):
    '''
    Find [T] that minimizes \sum_{pos in Crabs} |pos-T|
    The cost to change from T to T+1 is constant (is = 1)
    The total cost is the |# of pos > T| + |# of pos < T|
    So the best T has the same number of pos in each side
    So the best T is the median! 
    '''
    positions = sorted(map(int, data[0]))
    med = positions[len(positions)//2]

    return sum(abs(med-pos) for pos in positions)

@profiler
def part2(data):
    crabs = map(int, data[0])
    positions = Counter(crabs)

    min_cost = 1e9
    start, end = min(positions), max(positions) # best position must be inside the range [min(position), max(position)]
    for p in range(start, end+1):
        min_cost = min(min_cost, sum(positions[other_pos] * ( (abs(p-other_pos) * (abs(p-other_pos)+1) ) // 2 ) for other_pos in positions if other_pos  != p))

    return min_cost

@profiler
def part22(data):
    positions = list(map(int, data[0]))
    def cost(dst):
        return dst*(dst+1)//2

    min_cost = 1e9
    for target in range(min(positions), max(positions)+1):
        min_cost = min(min_cost, sum([cost(abs(x-target)) for x in positions]))
        
    return min_cost

if __name__=='__main__':
    data = parse_input('07')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')