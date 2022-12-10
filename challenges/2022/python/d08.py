'''

Advent of Code - 2022

--- Day 8: Treetop Tree House ---

'''

from utils import *

def parse_input(day):
    data = day_input(day)
    forest = defaultdict(lambda : -1)
    for y, line in enumerate(data):
        for x, tree in enumerate(line):
            forest[(x, y)] = int(tree)

    return forest

def is_visible(tree, forest):
    x, y, = tree[0], tree[1]
    height = forest[(x, y)]
    side = max(x[0] for x in forest)

    if all(forest[(i, y)] < height for i in range(x+1, side+1)):      #horizontal left to right: tree is visible if all tree to the right have smaller height
        return True
    if all(forest[(i, y)] < height for i in range(0, x)):             #horizontal right to left
        return True
    if all(forest[(x, i)] < height for i in range(0, y)):             #vertical top to bottom
        return True
    if all(forest[(x, i)] < height for i in range(y+1, side+1)):      #vertical bottom to top
        return True

    return False

@profiler
def part1(data):
    return len([tree for tree in data if is_visible(tree, data)])

def scenic_score(tree, forest):
    x, y, = tree[0], tree[1]
    height = forest[(x, y)]
    side = max(x[0] for x in forest)

    # tree is in one of the edges
    if x == 0 or y == 0 or x == side or y == side:
        return 0

    right, left, up, down = 0, 0, 0, 0
    other = -1
    # horizontal left to right
    for i in range(x+1, side+1):
        other = forest[(i, y)]
        if other < height:
            right += 1
        elif other >= height:
            right += 1
            break
    # horizontal right to left
    other = -1
    for i in range(x-1, -1, -1):
        other = forest[(i, y)]
        if other < height:
            left += 1
        elif other >= height:
            left += 1
            break

    # vertical top to bottom
    other = -1
    for i in range(y+1, side+1):
        other = forest[(x, i)]
        if other < height:
            down += 1
        elif other >= height:
            down += 1
            break

    # vertical bottom to top
    other = -1
    for i in range(y-1, -1, -1):
        other = forest[(x, i)]
        if other < height:
            up += 1
        elif other >= height:
            up += 1
            break

    return right * left * down * up

@profiler
def part2(data):
    return max([scenic_score(tree, data) for tree in data])

if __name__=='__main__':
    data = parse_input('08')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')