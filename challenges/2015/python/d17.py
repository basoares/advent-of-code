'''

Advent of Code - 2015

    --- Day 17: No Such Thing as Too Much ---

Released under the MIT License <http://opensource.org/licenses/mit-license.php>

'''

from re import findall
from itertools import combinations

def parse_input(containers):
    return list(map(int, containers))
    #return [int(c) for c in containers]

def part1(containers, target=150):
    cs = parse_input(containers)

    res = 0
    for i in range(len(cs)):
        for c in combinations(cs, i):
            if sum(c) == target:
                res += 1
    return res

def part12(containers, target=150):
    cs = parse_input(containers)

    res = 0
    for mask in range(1, 1 << len(cs)):
        p = [d for i, d in enumerate(cs) if (mask & ( 1 << i)) > 0]
        if sum(p) == target:
            res += 1

    return res

def part2(containers, target=150):
    cs = parse_input(containers)

    res = 0
    for i in range(len(cs)):
        for c in combinations(cs, i):
            if sum(c) == target:
                res += 1
        if res:
            return res

if __name__ == '__main__':
    with open('../input/d17.txt', mode='r') as f:
        _input = f.readlines()

        print('Part One: {}'.format(part1(_input)))
        #print('Part One: {}'.format(part12(_input)))
        print('Part Two: {}'.format(part2(_input)))
