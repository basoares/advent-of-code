'''

Advent of Code - 2015

--- Day 1: Not Quite Lisp ---

'''

tr = {'(': 1, ')': -1}

def part1(instructions):
    return sum(tr[i] for i in instructions)

def part2(instructions):
    floor = 0
    for idx, i in enumerate(instructions):
        floor += tr[i]

        if floor == -1:
            return idx+1

if __name__ == '__main__':
    with open('../input/d01.txt', mode='r') as f:
        _input = f.readline()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
