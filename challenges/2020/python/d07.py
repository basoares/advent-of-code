'''

Advent of Code - 2020

--- Day 7: Handy Haversacks  ---

'''

from utils import *
import re

def parse_input(day):
    data = day_input(day)
    bags = {}
    for line in data:
        rules = dict(line.split(' bags contain ') for line in data)
        for key, val in rules.items():
            values = []
            for n, bag in re.findall(r'(\d+) (\w+ \w+) bags?', val):
                values.append((bag, int(n)))
            rules[key] = values
        
    return rules

def part1(data, target='shiny gold'):
    parents = defaultdict(set)
    for parent, children in data.items():
        for child, _ in children:
            parents[child].add(parent)

    bags = deque([target])
    res = set()
    while bags:
        b = bags.popleft()
        for p in parents[b]:
            if p in res:
                continue
            bags.append(p)
            res.add(p)

    return len(res)
    
def part2(data):
    bags = deque([('shiny gold', 1)])
    total_bags = 0
    while bags:
        bag, num = bags.popleft()
        total_bags += num

        for child, n in data[bag]:
            bags.append((child, n*num))
    
    return total_bags-1
    
if __name__ == '__main__':
    data = parse_input('07')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
