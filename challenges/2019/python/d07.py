'''

Advent of Code - 2019

--- Day 7: Amplification Circuit ---

'''

from utils import *
from intcode import IntcodeRunner, HaltExecution

def parse_input(day):
    return day_input(day, integers)[0]

def part1(program):
    max_thruster = -1
    for p in permutations([0, 1, 2, 3, 4]):
        amplifiers = [IntcodeRunner(program).run() for i in range(5)]
        for i, amp in zip(p, amplifiers):
            next(amp)   
            amp.send(i)
    
        val = 0
        while True:
            try:
                for i, amp in enumerate(amplifiers):
                    val = amp.send(val)
                    if val and i == 4:
                        if max_thruster < val:
                            max_thruster = val 
            except StopIteration:
                #amplifiers.remove(amp)
                pass
            except HaltExecution:
                break

    return max_thruster

def part2(program):
    max_thruster = -1
    for p in permutations([5, 6, 7, 8, 9]):
        amplifiers = [IntcodeRunner(program, i).run() for i in range(5)]
        for i, amp in zip(p, amplifiers):
            next(amp)   
            amp.send(i)
        val = 0
        e = amplifiers[4]   #Amplifier E
        while True:
            try:
                for i, amp in enumerate(amplifiers):
                    val = amp.send(val)
                    if val and amp == e:
                        if max_thruster < val:
                            max_thruster = val
                    next(amp)
            except StopIteration:
                pass
            except HaltExecution:
                amplifiers.remove(amp)
                if not amplifiers:
                    break

    return max_thruster

if __name__ == '__main__':
    data = parse_input('07')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
