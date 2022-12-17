'''

Advent of Code - 2022

--- Day 10: Cathode-Ray Tube ---

'''

from utils import *

def parse_input(day):
    return day_input(day)

class HaltExecution(Exception):
    pass

class CPU:
    def __init__(self, X, memory):
        self.X = X
        self.memory = memory[:]
        self.cycle = 0
        self.pixels = ""
        self.halt = False

    def run(self):
        while not self.halt:
            if not self.memory:
                self.halt = True
                raise HaltExecution

            op = self.memory.pop(0)
            if op == 'noop':
                self.pixels += '#' if abs(self.X - (self.cycle % 40)) <= 1 else '.'
                self.cycle += 1
                yield self.cycle, self.X

            else:
                _, V = op.split()
                self.pixels += '#' if abs(self.X - (self.cycle % 40)) <= 1 else '.'
                self.cycle += 1
                yield self.cycle, self.X
                self.pixels += '#' if abs(self.X - (self.cycle % 40)) <= 1 else '.'
                self.cycle += 1
                yield self.cycle, self.X
                self.X += int(V)
                yield self.cycle, self.X

@profiler
def part1(data):
    res = 0
    seen = set()
    cpu = CPU(1, data)
    runner = cpu.run()

    while True:
        try:
            cycle, X = next(runner)
            if cycle in [20, 60, 100, 140, 180, 220] and cycle not in seen:
                res += X*cycle
                seen.add(cycle)
        except HaltExecution:
            break
    return res

def draw(pixels, lines=6, columns=40):
    for y in range(lines):
        row = []
        for x in range(columns):
            row.append(pixels[columns*y + x])
        print(''.join(row))

@profiler
def part2(data):
    cpu = CPU(1, data)
    runner = cpu.run()

    while True:
        try:
            next(runner)
        except HaltExecution:
            draw(cpu.pixels)
            #'BZPAJELK'
            return 0
    
if __name__=='__main__':
    data = parse_input('10')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')