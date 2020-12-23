'''

Advent of Code - 2020

--- Day 8: Handheld Halting  ---

'''

from utils import *

def parse_input(day):
    raw = day_input(day)
    return [(op, int(arg)) for line in raw for op, arg in (line.split(),)]

def boot(boot_code):
    ip = 0
    executed = set()
    accumulator = 0

    while ip < len(boot_code):
        if ip in executed:
            return accumulator, 'loop'
        else:
            executed.add(ip)

        op, arg = boot_code[ip]
        if op == 'nop':
            ip += 1
        elif op == 'acc':
            accumulator += arg
            ip += 1
        elif op == 'jmp':
            ip += arg
        else:
            raise ValueError(f'Invalid operation: {op}')

    return accumulator, 'halt'

def part1(data):
    acc, status = boot(data)
    assert status == 'loop'
    return acc

def part2(data):
    for ip, (op, arg) in enumerate(data):
        code = data[:]

        if op == 'nop':
            code[ip] = ('jmp', arg)
        elif op == 'jmp':
            code[ip] = ('nop', arg)
    
        acc, status = boot(code)
        if status == 'halt':
            return acc
    raise RuntimeError(f'Program never stops')

if __name__ == '__main__':
    data = parse_input('08')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
