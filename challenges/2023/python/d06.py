'''

Advent of Code - 2023

--- Day 6: Wait For It ---

'''

from utils import *

def parse_input(day):
    return day_input(day, integers) 

@profiler
def part1(data):
    times, distances = data
    races = zip(times, distances)
    
    ans = 1
    for time, distance in races:
        n = 0
        for t in range(time):
            if t*(time-t) > distance:
                n += 1
        ans *= n if n else 1
    return ans

@profiler
def part2(data):
    times, distances = data
    time = int(''.join([str(t) for t in times]))
    distance = int(''.join([str(d) for d in distances]))
    
    n = 0
    for t in range(time):
        if t*(time-t) > distance:
            n += 1
    return n
    
if __name__=='__main__':
    data = parse_input('06')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')