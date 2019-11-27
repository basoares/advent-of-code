'''

Advent of Code - 2015

    --- Day 9: All in a Single Night ---

'''

from collections import defaultdict
from itertools import permutations

def part1(distances):
    cities = set()
    pairs = defaultdict(int)

    for d in distances:
        src, _, dst, _, dist = d.split()

        pairs[(src, dst)] = int(dist)
        pairs[(dst, src)] = int(dist)

        cities.add(src)
        cities.add(dst)

    lengths = []
    for p in permutations(cities):
        lengths.append(sum(map(lambda x, y: pairs[(x, y)], p[:-1], p[1:])))

    return min(lengths)

def part2(distances):
    cities = set()
    pairs = defaultdict(int)

    for d in distances:
        src, _, dst, _, dist = d.split()

        pairs[(src, dst)] = int(dist)
        pairs[(dst, src)] = int(dist)

        cities.add(src)
        cities.add(dst)

    lengths = []
    for p in permutations(cities):
        lengths.append(sum(map(lambda x, y: pairs[(x, y)], p[:-1], p[1:])))

    return max(lengths)

if __name__ == '__main__':
    with open('../input/d09.txt', mode='r') as f:
        _input = f.readlines()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
