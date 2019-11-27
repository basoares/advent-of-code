'''

Advent of Code - 2015

    --- Day 13: Knights of the Dinner Table ---

'''

from re import findall
from collections import defaultdict
from itertools import permutations, tee

def parse_input(guest_list):
    happiness = defaultdict(int)
    guests = set()
    for g in guest_list:
    #x = match(r'(\S+) would (lose|gain) (\d+) happiness units by sitting next to (\S+)\.', g)
    #p1, change, value, p2 = x.group(1, 2, 3, 4)
        
        p1, change, value, p2 = findall(r'(\w+) \w+ (\w+) (\d+) .* (\w+)\.', g)[0]
        happiness[(p1, p2)] = int(value) * (1 if change == 'gain' else -1)
        guests.add(p1)

    return happiness, guests

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    iterable.append(next(iter(iterable), None)) #copy the first element to the last position so that a round table is simulated
    a, b = tee(iterable) 
    next(b, None)
    return zip(a, b)    

def happiness_change(guests, changes):
    return sum(changes[(a, b)]+changes[(b, a)] for (a, b) in pairwise(guests))

def part1(guest_list):
    happiness, guests = parse_input(guest_list)

    return max(happiness_change(list(p), happiness) for p in permutations(list(guests)))

def part2(guest_list):
    happiness, guests = parse_input(guest_list)

    #add ourselves to the lists by creating an extra pairs with zero change (everyone is ambivalence to our presence)
    for g in guests:
        happiness[(g, 'me')] = 0
    guests.add('me')

    return max(happiness_change(list(p), happiness) for p in permutations(list(guests)))

if __name__ == '__main__':
    with open('../input/d13.txt', mode='r') as f:
        _input = f.readlines()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
