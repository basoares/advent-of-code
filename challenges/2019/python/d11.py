'''

Advent of Code - 2019

--- Day 11: Space Police ---

'''

from utils import *
from intcode import IntcodeRunner, HaltExecution

def parse_input(day):
    return day_input(day, integers)[0]

turn = {
    ('u', 0): (),
    ('r', 0): () 

}

def part1(program):
    runner = IntcodeRunner(program)
    run = runner.run()
    grid = defaultdict(lambda: 0)
    x, y = (0, 0) #robot initial position
    direction = 'u' #robot initial direction

    while True: 
        try:
            next(run)
            color = run.send(grid[(x, y)])
            turn = run.send(None)
            grid[(x, y)] = color

            if turn: #turn right 90 degrees
                if direction == 'u':
                    direction = 'r'
                    x += 1
                elif direction == 'r':
                    direction = 'd'
                    y += 1
                elif direction == 'd':
                    direction = 'l'
                    x -= 1
                else:
                    direction = 'u'
                    y -= 1
            else:   #turn left 90 degrees
                if direction == 'u':
                    direction = 'l'
                    x -= 1
                elif direction == 'l':
                    direction = 'd'
                    y += 1
                elif direction == 'd':
                    direction = 'r'
                    x += 1
                else:
                    direction = 'u'
                    y -= 1

        except HaltExecution:
            break

    return len(grid.keys())

def part2(program):
    runner = IntcodeRunner(program)
    run = runner.run()
    grid = defaultdict(lambda: 0)
    x, y = (0, 0) #robot initial position
    grid[(x, y)] = 1
    direction = 'u' #robot initial direction

    while True: 
        try:
            next(run)
            color = run.send(grid[(x, y)])
            turn = run.send(None)
            grid[(x, y)] = color

            if turn: #turn right 90 degrees
                if direction == 'u':
                    direction = 'r'
                    x += 1
                elif direction == 'r':
                    direction = 'd'
                    y += 1
                elif direction == 'd':
                    direction = 'l'
                    x -= 1
                else:
                    direction = 'u'
                    y -= 1
            else:   #turn left 90 degrees
                if direction == 'u':
                    direction = 'l'
                    x -= 1
                elif direction == 'l':
                    direction = 'd'
                    y += 1
                elif direction == 'd':
                    direction = 'r'
                    x += 1
                else:
                    direction = 'u'
                    y -= 1

        except HaltExecution:
            break
    
    registration = [[' '] * 40 for i in range(10)]

    for x, y in [k for k, v in grid.items() if v == 1]:
        registration[2 + y][x] = '#'

    for row in registration:
        print(''.join(col*2 for col in row))

if __name__ == '__main__':
    data = parse_input('11')

    print(f'Part One: {part1(data)}')
    print(f'Part Two:')
    part2(data)

