'''

Advent of Code - 2023

--- Day 5: You Give A Seed A Fertilizer  ---

'''

from utils import *

def parse_input(day):
    seeds, *rest = day_input(day, delimiter='\n\n')
    seeds = [int(s) for s in seeds.split(':')[1].split()]
    maps = []
    for ranges in rest:
        r_maps = []
        for conv in ranges.splitlines()[1:]:
            dest, start, length = map(int, conv.split())
            r_maps.append((dest, start, length))
        maps.append(r_maps)
    return seeds, maps

@profiler
def part1(data):
    seeds, maps = data
    min_location = 99999999999999
    for seed in seeds:
        loc = seed
        for ranges in maps:
            for r in ranges:
                dest, start, length = r
                if loc in range(start, start+length+1):
                    loc = dest + (loc - start)
                    break
        min_location = min(min_location, loc)
    return min_location

@profiler
def part2(data):
    seeds, maps = data
    min_location = 99999999999999
    seed_ranges = zip(seeds[::2], seeds[1::2])
    for sr in seed_ranges:
        srs, sre = sr
    return min_location
    
if __name__=='__main__':
    data = parse_input('05')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')