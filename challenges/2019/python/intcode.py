'''

    Intcode interpreter for AoC 2019

'''

from enum import Enum
from utils import DynamicList

class Opcode(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUAL = 8
    RELATIVE_BASE = 9
    HALT = 99

class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2

class HaltExecution(Exception): pass

class IntcodeRunner:
    def __init__(self, program, pid=0):
        self.program = DynamicList(program[:])
        self.memory = DynamicList(program[:])
        self.ip = 0
        self.halt = False
        self.output = []
        self.pid = pid
        self.base_offset = 0

    def reset(self):
        self.ip = 0
        self.halt = False
        self.memory = self.program[:]
        self.output = []
        self.base_offset = 0

    def get_mem(self, position):
        return self.memory[position]
        
    def set_mem(self, position, value):
        self.memory[position] = value

    def fetch_instruction(self):
        instruction = self.memory[self.ip]

        #Instruction has format 'MMMMII' 
        #II represents the opcode
        opcode = instruction % 100

        #MMMM represent the parameter mode (in reverse order). Leading M are optional
        modes = [int(m) for m in f'{instruction//100:04}']
        modes = modes[::-1]

        return Opcode(opcode), modes

    def fetch_args(self, n_input_args, n_output_args, modes):
        args = []
        for i in range(n_input_args+n_output_args):
            arg = self.memory[self.ip+i]
            mode = Mode(modes[i])
            
            if mode == Mode.POSITION:
                if i < n_input_args:
                    args.append(self.memory[arg])
                else: #Parameters that an instruction writes to will never be in immediate mode
                    args.append(arg)
            elif mode == Mode.RELATIVE:
                if i < n_input_args:
                    args.append(self.memory[arg+self.base_offset])
                else: #Parameters that an instruction writes to will never be in immediate mode
                    args.append(arg+self.base_offset)
            elif mode == Mode.IMMEDIATE:
                args.append(arg)
            else:
                raise RuntimeError(f'Invalid parameter mode: {mode}')

        return args

    def run(self):
        while not self.halt:
            opcode, modes = self.fetch_instruction()
            #set ip to arguments location
            self.ip += 1

            #print('xxxx', opcode, modes, self.ip, self.output)
            if opcode == Opcode.ADD:
                #retrieve instruction parameters
                p1, p2, p3 = self.fetch_args(2, 1, modes)
                self.memory[p3] = p1+p2

                #set ip to next instruction
                self.ip += 3

            elif opcode == Opcode.MULTIPLY:
                #retrieve instruction parameters
                p1, p2, p3 = self.fetch_args(2, 1, modes)
                self.memory[p3] = p1*p2

                #set ip to next instruction
                self.ip += 3

            elif opcode == Opcode.INPUT:
                #retrieve instruction parameters
                p1, = self.fetch_args(0, 1, modes)
                
                self.memory[p1] = yield #block for input
                #print(f'Yield input: {self.pid} -> {self.memory[p1]}')

                #set ip to next instruction
                self.ip += 1
                assert self.memory[p1] is not None

            elif opcode == Opcode.OUTPUT:
                #retrieve instruction parameters
                p1, = self.fetch_args(1, 0, modes)
                self.output.append(p1)

                #set ip to next instruction
                self.ip += 1

                #print(f'Yield output: {self.pid} -> {p1}')
                yield p1
            
            elif opcode == Opcode.JUMP_IF_TRUE:
                p1, p2 = self.fetch_args(2, 0, modes)
                if p1:
                    self.ip = p2
                else:
                    self.ip += 2

            elif opcode == Opcode.JUMP_IF_FALSE:
                p1, p2 = self.fetch_args(2, 0, modes)
                if not p1:
                    self.ip = p2
                else:
                    self.ip += 2

            elif opcode == Opcode.LESS_THAN:
                p1, p2, p3 = self.fetch_args(2, 1, modes)
                if p1 < p2:
                    self.memory[p3] = 1
                else:
                    self.memory[p3] = 0

                #set ip to next instruction
                self.ip += 3

            elif opcode == Opcode.EQUAL:
                p1, p2, p3 = self.fetch_args(2, 1, modes)
                if p1 == p2:
                    self.memory[p3] = 1
                else:
                    self.memory[p3] = 0

                #set ip to next instruction
                self.ip += 3

            elif opcode == Opcode.RELATIVE_BASE:
                p1, = self.fetch_args(1, 0, modes)
                self.base_offset += p1

                #set ip to next instruction
                self.ip += 1

            elif opcode == Opcode.HALT:
                self.halt = True
                raise HaltExecution
                #self.ip += 1

            else:
                raise RuntimeError(f'Invalid opcode: {opcode}')
        