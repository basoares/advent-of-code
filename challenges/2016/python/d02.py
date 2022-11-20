'''

Advent of Code - 2016

--- Day 2: Bathroom Security ---

'''

from utils import *

def parse_input(day):
    return day_input(day)

def move(keypad, dir, x, y):
    if dir == 'U' and keypad[y-1][x] != '.': y -= 1 
    elif dir == 'D' and keypad[y+1][x] != '.': y += 1
    elif dir == 'L' and keypad[y][x-1] != '.':x -= 1
    elif dir == 'R' and keypad[y][x+1] != '.': x += 1

    return x, y

@profiler
def part1(data):
    keypad = """
    .....
    .123.
    .456.
    .789.
    .....
    """.split()

    ans = []

    for instruction in data:
        x, y = 2, 2 # position of the number 5 on the above keypad
        for i in instruction:
            x, y = move(keypad, i, x, y)
        ans.append(keypad[y][x])

    return ''.join(ans)

@profiler
def part2(data):
    keypad = """
    .......
    ...1...
    ..234..
    .56789.
    ..ABC..
    ...D...
    .......
    """.split()

    ans = []

    for instruction in data:
        x, y = 2, 2 # position of the number 5 on the above keypad
        for i in instruction:
            x, y = move(keypad, i, x, y)
        ans.append(keypad[y][x])

    return ''.join(ans)

if __name__=='__main__':
    data = parse_input('02')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')