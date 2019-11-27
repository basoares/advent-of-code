'''

Advent of Code - 2015

--- Day 2: I Was Told There Would Be No Math ---

'''

import re

def part1(presents):
    return sum(2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l) for (l, w, h) in presents)

def part2(presents):
    return sum(min(l+l+w+w, w+w+h+h, h+h+l+l) + l*w*h for (l, w, h) in presents)

if __name__ == '__main__':
    with open('../input/d02.txt', mode='r') as f:
        _input = f.readlines()

        presents = [tuple(map(int, re.findall(r'\d+', p))) for p in _input]

        print('Part One: {}'.format(part1(presents)))
        print('Part Two: {}'.format(part2(presents)))
