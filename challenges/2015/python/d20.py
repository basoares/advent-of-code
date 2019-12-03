'''

Advent of Code - 2015

    --- Day 20: Infinite Elves and Infinite Houses ---

'''

from collections import defaultdict

def factors(n): 
    return {f for i in range(1, int(n**0.5)+1) if n % i == 0 for f in [i, n//i]}

def part1(target=33100000):
    for h in range(target):
        num_presents = sum(factors(h)) * 10 #each elf delivers n*10 presents, where n is its own number
        if num_presents >= target:
            return h

def part2(target=33100000):
    elfs = defaultdict(int)
    for h in range(target):
        num_presents = 0
        for f in factors(h):
            if f not in elfs or elfs[f] <= 50:
                num_presents += f*11

            elfs[f] += 1
            if num_presents >= target:
                return h

if __name__ == '__main__':
    print('Part One: {}'.format(part1()))
    print('Part Two: {}'.format(part2()))
