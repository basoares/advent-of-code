'''

Advent of Code - 2024

--- Day 4: Ceres Search --- 

'''

from utils import *

def parse_input(day):
    data = day_input(day)
    return {(x, y): c for y, row in enumerate(data) for x, c in enumerate(row)}


@profiler
def part1(data):
    G = data
    total = 0
    for x, y in G.keys():
        if G[(x, y)] == 'X': # always look for the starting X to avoid double counts if looking for reversed word 
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx != 0 or dy != 0:
                        coords = [(x+dx*n, y+dy*n) for n in range(4)]
                        word = ''.join(G.get(c, '') for c in coords) 
                        if word == 'XMAS':
                            total += 1
    return total


@profiler
def part2(data):
    G = data
    total = 0
    for x, y in G.keys():
        if G[(x, y)] == 'A': 
            corner_letters = ''.join([G.get((x+x1, y+y1), '.') for x1, y1 in [(-1, -1), (1, -1), (1, 1), (-1, 1)]]) #get the letters that are on the 4 corners
            """
            M M  S M  S S  M S
             A    A    A    A
            S S  S M  M M  M S
            """
            if corner_letters in ['MMSS', 'SMMS', 'SSMM', 'MSSM']:
                total += 1
    return total

    
if __name__=='__main__':
    data = parse_input('04')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')