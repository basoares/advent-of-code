'''

Advent of Code - 2021

--- Day 13: Transparent Origami ---

'''

from utils import *

def parse_input(day):
    d, *i = day_input(day, delimiter='\n\n')
    dots = {tuple(map(int, dot.split(','))) for dot in d.split()}
    instructions = i[0].split('\n')

    return dots, instructions


def fold(dots, instruction):
    _, _, i = instruction.split()
    axis, p = i.split('=')
    
    if axis == 'x':
        return {(min(x, int(p)-(x-int(p))), y) for (x, y) in dots}
    elif axis == 'y':
        return {(x, min(y, int(p)-(y-int(p)))) for (x, y) in dots}
    else:
        raise RuntimeError(f'Invalid instruction: {instruction}')
    #if axis == 'y':
    #    return {(x, min(y, 2*int(p)-y)) for (x, y) in dots}
    #else:
    #    return {(min(x, 2*int(p)-x), y) for (x, y) in dots}

@profiler
def part1(data):
    dots, instructions = data
    return len(fold(dots, instructions[0]))

                
@profiler
def part2(data):
    dots, instructions = data
    for i in instructions:
        dots = fold(dots, i)

    X, Y = map(max, zip(*dots))
    for y in range(Y+1):
        print(*[' #'[(x, y) in dots] for x in range(X+1)])

if __name__=='__main__':
    data = parse_input('13')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')