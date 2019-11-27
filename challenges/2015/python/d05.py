'''

Advent of Code - 2015

--- Day 5: Doesn't He Have Intern-Elves For This? ---

'''

from itertools import groupby
import re

def part1(strings):
    nice = 0
    for s in strings:
        #does not contain 3 or more vowels
        if sum(1 for c in s if c in 'aeiou') < 3: 
            continue
        #does not contain at least one letter that appears twice in a row
        #if not [x for x, grp in groupby(s) if sum(1 for _ in grp) >= 2]: 
        #    continue
        #does not contain at least one letter that appears twice in a row
        if not re.search(r'([a-z])\1', s):
            continue
        #contains one of the strings 'ab', 'cd', 'pq', 'xy'
        if any(x in s for x in ['ab', 'cd', 'pq', 'xy']):
            continue

        nice += 1

    return nice

def string_parts(string, n):
    return [string[i:i+n] for i in range(len(s)-n+1)]

def part2(strings):
    return sum(1 for s in strings if re.search(r'([a-z]{2}).*\1', s) and re.search(r'([a-z]).\1', s))

if __name__ == '__main__':
    with open('../input/d05.txt', mode='r') as f:
        _input = f.readlines()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
