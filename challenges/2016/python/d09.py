'''

Advent of Code - 2016

--- Day 9: Explosives in Cyberspace ---

'''

from utils import *

def parse_input(day):
    raw = day_input(day)[0]
    # remove white spaces
    return re.sub('\s', '', raw)

def decompress(file, recursive=False):
    length = 0
    i = 0
    while i < len(file):
        m = re.match(r'\((\d+)x(\d+)\)', file[i:])
        if m:
            n, r = map(int, m.groups())
            i += m.end()
            length += r * ( decompress(file[i:i+n], recursive) if recursive else n)
            i += n 
        else:
            length += 1
            i += 1
    return length 

@profiler
def part1(data):
    return decompress(data)

@profiler
def part2(data):
    return decompress(data, True)

if __name__=='__main__':
    data = parse_input('09')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
