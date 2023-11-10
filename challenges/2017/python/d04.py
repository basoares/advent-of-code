'''

Advent of Code - 2017

--- Day 4: High-Entropy Passphrases ---

'''

from utils import *

def parse_input(day):
    return day_input(day)

@profiler
def part1(data):
    #return sum(1 for passphrase in data if max(Counter(passphrase.split()).values()) == 1 )
    return sum(1 for p in data if len(set(p.split())) == len(p.split()))

@profiler
def part2(data):
    #return sum(1 for passphrase in data if max(Counter([''.join(sorted(p)) for p in passphrase.split()]).values()) == 1 )
    return sum(1 for passphrase in data if len(set([''.join(sorted(p)) for p in passphrase.split()])) == len(passphrase.split()))


if __name__=='__main__':
    data = parse_input('04')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')