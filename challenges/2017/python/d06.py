'''

Advent of Code - 2017

--- Day 6: Memory Reallocation ---

'''

from utils import *

def parse_input(day):
    return day_input(day, parser=integers)[0]


def reallocate(blocks, memory_banks):
    max_blocks = max(blocks)
    idx = blocks.index(max_blocks)
    blocks[idx] = 0
    for n in range(max_blocks):
        blocks[(idx+n+1) % memory_banks] += 1

    return tuple(blocks)

@profiler
def part1(data, memory_banks=16):
    blocks = data[:]
    seen = { tuple(blocks) }
    for cycle in count(1):
        block = reallocate(blocks, memory_banks)
        if block in seen:
            return cycle
        seen.add(block)

@profiler
def part2(data, memory_banks=16):
    blocks = data[:]
    seen = { tuple(blocks): 0 }

    for cycle in count(1):
        block = reallocate(blocks, memory_banks)
        if block in seen:
            return cycle - seen[block]
        seen[block] = cycle

if __name__=='__main__':
    data = parse_input('06')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')