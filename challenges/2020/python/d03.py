'''

Advent of Code - 2020

--- Day 3: Toboggan Trajectory ---

'''

from utils import day_input

def parse_input(day):
    return day_input(day)

def part1(data, down=1, right=3):
    trees = 0

    r = 0 
    for d in range(0, len(data), down):
        if data[d][r % len(data[d])] == '#':
            trees += 1
        r += right
    return trees

def part12(data):
    return sum(slope[right*3 % len(slope)] == '#' for right, slope in enumerate(data))

def part2(data):
    right_down = [(1, 1), (3, 1) , (5, 1), (7, 1), (1, 2)]

    res = 1
    for right, down in right_down:
        trees = 0
        r = 0 
        for d in range(0, len(data), down):
            if data[d][r % len(data[d])] == '#':
                trees += 1
            r += right
        res *= trees
    return res
    
if __name__ == '__main__':
    data = parse_input('03')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
