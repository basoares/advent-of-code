'''

Advent of Code - 2024

--- Day 6: Guard Gallivant --- 

'''

from utils import *

def parse_input(day):
    data = day_input(day)
    G = defaultdict(lambda: "")
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c in '>v<^':
                guard = (x, y)
                d = c
            G[(x, y)] = c
    return G, guard, d

dirs = {'^': (0, -1), '<': (-1, 0), 'v': (0, 1), '>': (1, 0)}
turn = {'>': 'v', 'v': '<', '<': '^', '^': '>'}

def walked_path(G, guard, d):
    seen = set()
    while True:
        x, y = guard
        seen.add((x, y))
        new_pos = (x+dirs[d][0], y+dirs[d][1])
        if new_pos not in G: #guard has left the area.
            break
        elif G[new_pos] == '#':
            d = turn[d]
        else:
            seen.add(new_pos)
            guard = new_pos
    return seen

@profiler
def part1(data):
    G, guard, d = data
    return len(walked_path(G, guard, d))
    
@profiler
def part2(data):
    G, guard, d = data
    guard_start, d_start = guard, d
    seen = walked_path(G, guard, d)

    # obstacles must be placed in path originally walked by the guard, otherwise it is not possible to create a loop
    res = 0
    seen.remove(guard_start) # remove guard start position as it cannot have any obstacle
    for coord in seen:
        G[coord] = '#' # add an obstacle
        seen_loop = set()
        guard = guard_start
        d = d_start
        while True:
            x, y = guard
            seen_loop.add((guard, d))
            new_pos = (x+dirs[d][0], y+dirs[d][1])
            if new_pos not in G: # no loop. exit
                break
            elif G[new_pos] == '#':
                d = turn[d]
            else:
                if (new_pos, d) in seen_loop: # if same position and direction, there is a loop. start next
                    res += 1
                    break
                seen_loop.add((new_pos, d))
                guard = new_pos
        G[coord] = '.' # reset the grid by removing the obstacle
    return res
        
if __name__=='__main__':
    data = parse_input('06')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')