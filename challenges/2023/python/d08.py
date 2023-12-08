'''

Advent of Code - 2023

--- Day 8: Haunted Wasteland ---

'''

from utils import *

def parse_input(day):
    instructions, rest = day_input(day, delimiter='\n\n')
    nodes = {}
    for node in rest.splitlines():
        start, left, right = re.match(r'(\w+) = \((\w+), (\w+)\)', node).groups()
        nodes[start] = (left, right)
    return instructions, nodes

@profiler
def part1(data):
    instructions, nodes = data
    current = 'AAA'
    for i, instr in enumerate(cycle(instructions)):
        current = nodes[current][0] if instr == 'L' else nodes[current][1]
        if current == 'ZZZ':
            return i+1

@profiler
def part2(data):
    instructions, nodes = data
    start_nodes = [node for node in nodes if node.endswith('A')]
    steps = []
    for node in start_nodes:
        current = node
        for i, instr in enumerate(cycle(instructions)):
            current = nodes[current][0] if instr == 'L' else nodes[current][1]
            if current.endswith('Z'):
                steps.append(i+1)
                break
    
    return list(accumulate(steps, lcm))[-1]

if __name__=='__main__':
    data = parse_input('08')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')