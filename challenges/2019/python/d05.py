'''

Advent of Code - 2019

    --- Day 5: Sunny with a Chance of Asteroids ---

'''

from utils import *


class IntcodeRunner:
    def __init__(self, program):
        self.program = program[:]
        self.memory = program[:]
        self.ip = 0 
        self.halt = False
        self.output = []

    def reload(self):
        self.ip = 0
        self.halt = False
        self.memory = self.program[:]

    def set_mem(self, position, value):
        self.memory[position] = value

    def fetch_instruction(self):
        return self.memory[self.ip]

    def immediate_or_memory(self, parameter, mode):
        '''Immediate mode (1) parameter is interpreted as a value 
        Position mode (0) return value stored at address "parameter" in memory
        '''
        return parameter if int(mode) else self.memory[parameter]

    def step(self, input_instruction):
        instruction = self.fetch_instruction()

        #Instruction has format 'MMMMII' 
        #II represents the opcode
        opcode = instruction % 100

        #MMMM represent the parameter mode (in reverse order). Leading M are optional
        modes = f'{instruction//100:04}'
        modes = modes[::-1]

        if opcode == 1:
            #retrieve instruction parameters
            p1, p2, p3 = self.memory[self.ip+1:self.ip+4]
            self.memory[p3] = self.immediate_or_memory(p1, modes[0])+self.immediate_or_memory(p2, modes[1])

            #set ip to next instruction
            self.ip += 4

        elif opcode == 2:
            #retrieve instruction parameters
            p1, p2, p3 = self.memory[self.ip+1:self.ip+4]
            self.memory[p3] = self.immediate_or_memory(p1, modes[0])*self.immediate_or_memory(p2, modes[1])

            #set ip to next instruction
            self.ip += 4

        elif opcode == 3:
            #retrieve instruction parameters
            p1 = self.memory[self.ip+1]
            self.memory[p1] = input_instruction

            #set ip to next instruction
            self.ip += 2

        elif opcode == 4:
            #retrieve instruction parameters
            p1 = self.memory[self.ip+1]
            self.output.append(self.immediate_or_memory(p1, modes[0]))

            #set ip to next instruction
            self.ip += 2
        
        elif opcode == 5:
            p1, p2 = self.memory[self.ip+1:self.ip+3]
            if self.immediate_or_memory(p1, modes[0]):
                self.ip = self.immediate_or_memory(p2, modes[1])
            else:
                self.ip += 3

        elif opcode == 6:
            p1, p2 = self.memory[self.ip+1:self.ip+3]
            if not self.immediate_or_memory(p1, modes[0]):
                self.ip = self.immediate_or_memory(p2, modes[1])
            else:
                self.ip += 3

        elif opcode == 7:
            p1, p2, p3 = self.memory[self.ip+1:self.ip+4]
            if self.immediate_or_memory(p1, modes[0]) < self.immediate_or_memory(p2, modes[1]):
                self.memory[p3] = 1
            else:
                self.memory[p3] = 0

            #set ip to next instruction
            self.ip += 4

        elif opcode == 8:
            p1, p2, p3 = self.memory[self.ip+1:self.ip+4]
            if self.immediate_or_memory(p1, modes[0]) == self.immediate_or_memory(p2, modes[1]):
                self.memory[p3] = 1
            else:
                self.memory[p3] = 0

            #set ip to next instruction
            self.ip += 4

        elif opcode == 99:
            self.halt = True
            self.ip += 1

        else:
            raise RuntimeError(f'Invalid opcode: {opcode}')

    def run(self, input_instruction):
        while not self.halt:
            self.step(input_instruction)

        return self.memory[0], self.output

def parse_input(day):
    return day_input(day, integers)[0]

def part1(program, input_instruction=1):
    runner = IntcodeRunner(program)
    _, output = runner.run(input_instruction)
    return output[-1]
    

def part2(program, input_instruction=5):
    runner = IntcodeRunner(program)
    _, output = runner.run(input_instruction)
    return output[-1]
            
if __name__ == '__main__':
    data = parse_input('05')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
