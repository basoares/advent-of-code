'''

Advent of Code - 2017

--- Day 5: A Maze of Twisty Trampolines, All Alike ---

'''

from utils import *

def parse_input(day):
    #return [0, 3, 0, 1, -3]
    return day_input(day, parser=int)

@profiler
def part1(data):
    tape = data[:]
    steps = pc = 0
    while 0 <= pc < len(tape):
        steps += 1
        prevpc = pc
        pc += tape[pc]
        tape[prevpc] += 1
    return steps

@profiler
def part2(data):
    tape = data[:]
    steps = pc = 0
    while 0 <= pc < len(tape):
        steps += 1
        oldpc = pc
        pc += tape[pc]
        if tape[oldpc] >= 3:
            tape[oldpc] += -1
        else:
            tape[oldpc] += 1
    return steps

if __name__=='__main__':
    data = parse_input('05')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')