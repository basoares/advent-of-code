'''

Advent of Code - 2016

--- Day 8: Two-Factor Authentication ---

'''

from utils import *

def parse_input(day):
    return day_input(day)

rows = 6
columns = 50

def rotate(screen, row, shifts):
    b = -1 * (shifts % columns)
    screen[row] = screen[row][b:] + screen[row][:b]
    return screen


def process(screen, instruction):
    a, b = map(int, re.findall(r'\d+', instruction))
    if 'rect' in instruction:
        for i in range(b):
            screen[i] = [1]*a + screen[i][a:]
    elif 'row' in instruction:
        screen = rotate(screen, a, b)
    elif 'column' in instruction:
        tr = list(map(list, zip(*screen)))
        rotate(tr, a, b)
        screen = list(map(list, zip(*tr)))

    return screen


@profiler
def part1(data):
    screen = [[0]*columns]*rows
    for instruction in data:
        screen = process(screen, instruction)

    return sum(sum(s) for s in screen)


@profiler
def part2(data):
    def printscreen(screen):
        for y in range(rows):
            print(''.join('*' if x == 1 else ' ' for x in screen[y]))

    screen = [[0]*columns]*rows
    for instruction in data:
        screen = process(screen, instruction)

    printscreen(screen)


if __name__=='__main__':
    data = parse_input('08')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')