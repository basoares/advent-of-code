'''

Advent of Code - 2022

--- Day 12: Hill Climbing Algorithm ---

'''

from utils import *

def parse_input(day):
    raw = day_input(day)
    heightmap = defaultdict(int)
    for y, line in enumerate(raw):
        for x, h in enumerate(line):
            heightmap[(x, y)] = h

    S = [k for k,v in heightmap.items() if v == 'S'][0]
    heightmap[S] = 'a'
    E = [k for k,v in heightmap.items() if v == 'E'][0]
    heightmap[E] = 'z'
    return heightmap, S, E


@profiler
def part1(data):
    grid, S, E = data

    visited = defaultdict(int)
    visited[S] = 0
    q = deque([S])
    while q:
        pos = q.popleft()
        for c in neighbors4(pos):
            if c in grid:
                if ord(grid[c]) <= ord(grid[pos]) + 1:
                    if c == E:
                        return visited[pos]+1
                    if c not in visited:
                        q.append(c)
                        visited[c] = visited[pos] + 1
                
    raise ValueError(r'No path was found')


@profiler
def part2(data):
    grid, _, E = data
    a_pos = [k for k,v in grid.items() if v == 'a']

    distances_from_a = defaultdict(int)
    for a in a_pos:
        visited = defaultdict(int)
        visited[a] = 0
        q = deque([a])
        while q:
            pos = q.popleft()
            if pos == E:
                distances_from_a[a] = visited[pos]
                break
            
            for c in neighbors4(pos):
                if c in grid:
                    if ord(grid[c]) <= ord(grid[pos]) + 1:
                        if c not in visited:
                            q.append(c)
                            visited[c] = visited[pos] + 1

    return min(distances_from_a.values())
    
    
if __name__=='__main__':
    data = parse_input('12')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')