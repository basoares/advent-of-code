'''

Advent of Code - 2025

--- Day 4: Printing Department --- 

'''

from utils import *

def parse_input(day):
    return {(x, y): c for y, row in enumerate(day_input(day)) for x, c in enumerate(row)}


@profiler
def part1(data):
    G = data
    rolls = 0
    for (x, y), c in G.items():
        rs = 0
        if c == '@':
            for n in neighbors8((x, y)):
                if n in G and G[n] == '@':
                    rs += 1
            if rs < 4:
                rolls += 1
    return rolls


@profiler
def part2(data):
    G = data
    rolls = 0
    removed = True
    while removed:
        removed = False
        for xy, c in G.items():
            rs = 0
            if c == '@':
                for n in neighbors8(xy):
                    if n in G and G[n] == '@':
                        rs += 1
                if rs < 4:
                    rolls += 1
                    G[xy] = '.'
                    removed = True
    return rolls

    
if __name__=='__main__':
    data = parse_input('04')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')