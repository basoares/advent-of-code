'''

Advent of Code - 2025

--- Day 2: Gift Shop --- 

'''

from utils import *

def parse_input(day):
    parser = lambda x: tuple(map(int, re.findall(r'\d+', x)))
    return day_input(day, parser=parser, delimiter=',')


def invalid(id):
    return id[:len(id)//2] == id[len(id)//2:]
    

@profiler
def part1(data):
    res = 0
    for start, end in data:
        for id in range(start, end+1):
            if invalid(str(id)):
                res += id
    return res


@profiler
def part2(data):
    res = 0
    for start, end in data:
        for id in range(start, end+1):
            x = str(id)
            # https://leetcode.com/problems/repeated-substring-pattern/description/
            # If s = t repeated k times with k>1, then shifting s by |t| characters produces a string equal to s but starting at a different point. 
            # That shifted version appears inside s+s, and removing first and last characters doesn't remove that shifted copy. 
            # If s is not a repetition, no such shifted copy exists, so s won't appear in (s+s)[1:-1].
            if x in (x+x)[1:-1]:
                res += id
    return res 

    
if __name__=='__main__':
    data = parse_input('02')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')