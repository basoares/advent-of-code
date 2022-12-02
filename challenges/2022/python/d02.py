'''

Advent of Code - 2022

--- Day 2: Rock Paper Scissors ---

'''

from utils import *

def parse_input(day):
    parser = lambda line : re.match(r'(\w) (\w)', line).groups()
    return day_input(day, parser)

points = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
opponent = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}

@profiler
def part1(data):
    response = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
    win = {
        ('Rock', 'Rock'): 3, ('Rock', 'Paper'): 6, ('Rock', 'Scissors'): 0,
        ('Paper', 'Paper'): 3, ('Paper', 'Scissors'): 6, ('Paper', 'Rock'): 0,
        ('Scissors', 'Scissors'): 3, ('Scissors', 'Rock'): 6, ('Scissors', 'Paper'): 0
    }
    
    return sum(win[(opponent[a], response[b])] + points[response[b]] for a, b in data)

@profiler
def part2(data):
    response = {'X': 0, 'Y': 3, 'Z': 6}
    win = {
        ('Rock', 6): 'Paper', ('Rock', 3): 'Rock', ('Rock', 0): 'Scissors',
        ('Paper', 6): 'Scissors', ('Paper', 3): 'Paper', ('Paper', 0): 'Rock',
        ('Scissors', 6): 'Rock', ('Scissors', 3): 'Scissors', ('Scissors', 0): 'Paper'
    }
    return sum(points[(win[opponent[a], response[b]])] + response[b] for a, b in data)

if __name__=='__main__':
    data = parse_input('02')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')