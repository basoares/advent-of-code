'''

Advent of Code - 2015

    --- Day 19: Medicine For Rudolph ---

'''

import re
from random import choice

def parse_input(config):
    replacements = []
    for c in config:
        if c:
            m = re.findall(r'(\w+) => (\w+)', c)
            if m:
                replacements.append(m[0])
            else:
                molecule = c

    return replacements, molecule

def part1(config):
    replacements, molecule = parse_input(config)
    
    results = set()
    for a, b in replacements:
        for m in range(len(molecule)):
            if a == molecule[m:m+len(a)]:
                results.add(molecule[:m] + b + molecule[m+len(a):])
    return len(results)


def part2(config):
    reps, molecule = parse_input(config)

    replacements = [(b, a) for (a, b) in reps]
    
    steps = 0
    #looping over the replacement list resulted in molecules that were different from 'e' but could not be further replaced
    #by selecting one random replacement rule in each iteration, I was able to get a result
    while molecule != 'e':
        k, v = choice(replacements)
        if k in molecule:
            molecule = molecule.replace(k, v, 1)
            steps += 1
        print(len(molecule))

    return steps

if __name__ == '__main__':
    with open('../input/d19.txt', mode='r') as f:
        _input = f.readlines()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
