'''

Advent of Code - 2015

    --- Day 10: Elves Look, Elves Say ---

'''

from itertools import groupby

def part1(sequence='3113322113'):
    for _ in range(40):
        sequence = ''.join([str(len(list(g))) + str(k) for k, g in groupby(sequence)])

    return len(sequence)

def part2(sequence='3113322113'):
    for _ in range(50):
        sequence = ''.join([str(len(list(g))) + str(k) for k, g in groupby(sequence)])

    return len(sequence)

if __name__ == '__main__':
    with open('../input/d10.txt', mode='r') as f:
        _input = f.readline()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
