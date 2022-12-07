'''

Advent of Code - 2022

--- Day 7: No Space Left On Device ---

'''

from utils import *

def parse_input(day):
    return day_input(day)

def parent_dirs(dir):
    path = dir[:]
    while path:
        yield '/'.join(path)
        path.pop()

@profiler
def part1(data):
    directories = defaultdict(int)
    for cmd in data:
        match cmd.split():
            case '$', 'cd', '/': 
                path = ['/']
            case '$', 'cd', '..': 
                path.pop()
            case '$', 'cd', dir: 
                path.append(dir)
            case '$', 'ls': 
                pass 
            case 'dir', d: 
                pass
            case size, filename:
                for p in parent_dirs(path):
                    directories[p] += int(size)

    #return directories
    return sum(s for s in directories.values() if s <= 100000)

@profiler
def part2(data):
    directories = defaultdict(int)
    for cmd in data:
        match cmd.split():
            case '$', 'cd', '/': 
                path = ['/']
            case '$', 'cd', '..': 
                path.pop()
            case '$', 'cd', dir: 
                path.append(dir)
            case '$', 'ls': 
                pass 
            case 'dir', d: 
                pass
            case size, filename:
                for p in parent_dirs(path):
                    directories[p] += int(size)

    root = directories['/']
    return min(size for size in directories.values() if 70000000 - root + size >= 30000000)

if __name__=='__main__':
    data = parse_input('07')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')