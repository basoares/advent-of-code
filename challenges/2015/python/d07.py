'''

Advent of Code - 2015

    --- Day 7: Some Assembly Required ---

Released under the MIT License <http://opensource.org/licenses/mit-license.php>

'''

from collections import defaultdict
import re

operations = {
            None: lambda arg0, arg1: None,
           'AND': lambda arg0, arg1: arg0 & arg1,
        'LSHIFT': lambda arg0, arg1: arg0 << arg1,
           'NOT': lambda arg0, arg1: ~arg0 & 0xffff,
            'OR': lambda arg0, arg1: arg0 | arg1,
        'RSHIFT': lambda arg0, arg1: arg0 >> arg1,
           'SET': lambda arg0, arg1: arg0
        }

def parse_instructions(booklet):
    instructions = defaultdict()
    for line in booklet:
        a, b = line.strip().split(' -> ')
        res = a.split()
        if len(res) == 1:
            x = res[0]
            op = 'SET'
            y = None
        elif len(res) == 2:
            op = res[0]
            x = res[1]
            y = None
        elif len(res) == 3:
            x, op, y = res
        
        #each wire can only get a signal from one source
        instructions[b] = (op, x, y)

    return instructions

def calculate(instructions, wires, w):
    try:
        return int(w)
    except ValueError:
        pass
    except TypeError:
        return None

    if w not in wires:
        op, x, y = instructions[w] 
        wires[w] = operations[op](calculate(instructions, wires, x), calculate(instructions, wires, y))

    return wires[w]

def part1(booklet):
    wires = defaultdict(int)
    instructions = parse_instructions(booklet)
    
    return calculate(instructions, wires, 'a')

def part2(booklet):
    wires = defaultdict(int)
    instructions = parse_instructions(booklet)
    
    a = calculate(instructions, wires, 'a')
    wires = defaultdict(int)
    wires['b'] = a

    return calculate(instructions, wires, 'a')

if __name__ == '__main__':
    with open('../input/d07.txt', mode='r') as f:
        _input = f.readlines()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
