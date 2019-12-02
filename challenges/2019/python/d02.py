'''

Advent of Code - 2019

    --- Day 2: 1202 Program Alarm ---

'''

from utils import *

class IntcodeRunner:
    def __init__(self, program):
        self.program = program
        self.ip = 0 
        self.halt = False

    def set_mem(self, position, value):
        self.program[position] = value

    def fetch_instruction(self):
        return self.program[self.ip]

    def step(self):
        opcode = self.fetch_instruction()

        if opcode == 1:
            #retrieve instruction parameters
            p1, p2, p3 = self.program[self.ip+1:self.ip+4]
            self.program[p3] = self.program[p1]+self.program[p2]

            #set ip to next instruction
            self.ip += 4

        elif opcode == 2:
            #retrieve instruction parameters
            p1, p2, p3 = self.program[self.ip+1:self.ip+4]
            self.program[p3] = self.program[p1]*self.program[p2]

            #set ip to next instruction
            self.ip += 4
        
        elif opcode == 99:
            self.halt = True
            self.ip += 1

    def run(self):
        while not self.halt:
            self.step()

        return self.program[0]

def parse_input(day):
    return day_input(day, integers)[0]

def part1(program, noun=12, verb=2):
    runner = IntcodeRunner(program[:])
    runner.set_mem(1, noun)
    runner.set_mem(2, verb)

    return runner.run()

def part2(program, target=19690720):
    for noun in range(100, -1, -1):
        for verb in range(100):
            runner = IntcodeRunner(program[:])
            runner.set_mem(1, noun)
            runner.set_mem(2, verb)

            if runner.run() == target:
                return 100*noun+verb

if __name__ == '__main__':
    data = parse_input('02')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
