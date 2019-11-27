'''

Advent of Code - 2015

    --- Day 12: JSABacusFramework.io ---

'''

import re
import json

def part1(obj):
    return sum(map(int, re.findall(r'-?\d+', obj)))

def sum_json(obj):
    if type(obj) is int:
        return obj

    if type(obj) is list:
        return sum(map(sum_json, obj))

    if type(obj) is dict:
        vals = obj.values()

        if 'red' in vals:
            return 0
        
        return sum(map(sum_json, vals))
    else: 
        return 0

def part2(obj):
    return sum_json(json.loads(obj))

if __name__ == '__main__':
    with open('../input/d12.txt', mode='r') as f:
        _input = f.readline()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
