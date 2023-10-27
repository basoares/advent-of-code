'''

Advent of Code - 2022

--- Day 13: Distress Signal ---

'''

from utils import *
from functools import cmp_to_key

def parse_part(line):
    part = []
    for idx, p in enumerate(line[1:-1].split(',')):
        if p.startswith('['):
            part.append(parse_part(line[idx+1:]))
        elif p[-1] == ']':
            return part
        else:
            part.append(int(p))
    return part

def parse_input(day):
    return day_input(day, delimiter='\n\n')

def right_order(pack1, pack2):
    # if different types change int to list
    if type(pack1) != type(pack2):
        if type(pack1) is int:
            pack1 = [pack1]
        else:
            pack2 = [pack2]
    elif type(pack1) is int:
        if pack1 < pack2:
            return -1
        elif pack1 == pack2:
            return 0
        else:
            return 1

    for a, b in zip(pack1, pack2):
        ro = right_order(a, b)
        if ro:
            return ro

    if len(pack1) != len(pack2):
        return -1 if len(pack1) < len(pack2) else 1
    else:
        return 0 

@profiler
def part1(data):
    # use python eval to parse and evaluate the input
    pairs = [(eval(pair.split()[0]), eval(pair.split()[1])) for pair in data]
    return sum(idx+1 for idx, pair in enumerate(pairs) if right_order(pair[0], pair[1]) == -1)

@profiler
def part2(data):
    packets = [eval(packet) for pair in data for packet in pair.split()]
    packets.extend([[[2]], [[6]]])

    packets.sort(key=cmp_to_key(right_order))
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1) 

if __name__=='__main__':
    data = parse_input('13')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')