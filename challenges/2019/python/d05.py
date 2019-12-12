'''

Advent of Code - 2019

    --- Day 5: Sunny with a Chance of Asteroids ---

'''

from utils import *
from intcode import IntcodeRunner, HaltExecution

def parse_input(day):
    return day_input(day, integers)[0]

def part1(program, input_instruction=1):
    runner = IntcodeRunner(program)
    run = runner.run()
    while True:
        try:
            next(run)
            run.send(input_instruction)
        except HaltExecution:
            break
    
    return runner.output

def part2(program, input_instruction=5):
    runner = IntcodeRunner(program)
    run = runner.run()
    while True:
        try:
            next(run)
            run.send(input_instruction)
        except HaltExecution:
            break

    return runner.output
            
if __name__ == '__main__':
    data = parse_input('05')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
