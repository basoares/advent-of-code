'''

Advent of Code - 2022

--- Day 5: ---

'''

from utils import *

def parse_input(day):
    return day_input(day, parser=str, delimiter='\n\n')

def parse_stacks(data):
    '''
    stacks = list(
    "".join(x).strip()[1:]
        for i, x in enumerate(
            zip(*map(list, stacks.split("\n")[::-1]))
        )
        if i % 4 == 1
    )'''
    stacks = {k: [] for k in range(1, 10)}
    for line in data.split("\n"):
        for i, crate in enumerate(line[1::4]):
            if crate != ' ' and crate not in "123456789":
                stacks[i+1].append(crate)

    return stacks

@profiler
def part1(data):
    raw, moves = data
    stacks = parse_stacks(raw)

    for move in moves.split("\n"):
        n, source, dest = digits(move)
        for _ in range(int(n)):
            crate = stacks[int(source)].pop(0)
            stacks[int(dest)].insert(0, crate)

    #res = []
    #ks = stacks.keys()
    #for k in sorted(ks): 
    #    res.append(stacks[k].pop(0))

    #return ''.join(res)
    #PSNRGBTFT
    return ''.join(stacks[s][0] for s in stacks if stacks[s])

@profiler
def part2(data):
    raw, moves = data
    stacks = parse_stacks(raw)

    for move in moves.split("\n"):
        n, source, dest = digits(move)
        crates = stacks[int(source)][:n]
        del stacks[int(source)][:n]
        stacks[int(dest)][0:0] = crates

    #BNTZFPMMW
    return ''.join(stacks[s][0] for s in stacks if stacks[s])

if __name__=='__main__':
    data = parse_input('05')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')