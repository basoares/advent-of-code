'''

Advent of Code - 2023

--- Day 2: Cube Conundrum  --- 

'''

from utils import *

def parse_input(day):
    def parse_game(line):
        x, xs = line.split(': ')
        id = x.split()[1]
        return id, [cubes.split(', ') for cubes in xs.split('; ')]
    return day_input(day, parser=parse_game)

def valid_game(game):
    m = {'red': 12, 'green': 13, 'blue': 14}
    for cubes in game:
        for cube in cubes:
            n, c = cube.split(' ')
            if int(n) > int(m[c]):
                return False
    return True

@profiler
def part1(data):
    return sum(int(id) for id, game in data if valid_game(game))

def find_max(game):
    max_color = { 'red': 0, 'green': 0, 'blue': 0 }
    for cubes in game:    
        for cube in cubes:
            n, c = cube.split()
            max_color[c] = max(max_color[c], int(n))

    return max_color.values()

@profiler
def part2(data):
    return sum(prod(find_max(game)) for _, game in data)
    
if __name__=='__main__':
    data = parse_input('02')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')