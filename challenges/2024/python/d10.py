'''

Advent of Code - 2024

--- Day 10: Hoof It --- 

'''

from utils import *

def parse_input(day):
    data = day_input(day)
    return {(x, y): c for y, row in enumerate(data) for x, c in enumerate(row)}


def num_trails(s, G, part1=True):
    seen = set([s])
    queue = deque([(s, 0)])

    trails = 0
    while queue:
        point, h = queue.popleft()
        for n in neighbors4(point):
            if n in G and G[n] != '.' and int(G[n]) == h+1 and n not in seen:
                if int(G[n]) == 9:
                    trails += 1
                    if part1:
                        seen.add(n)
                else:
                    if part1:
                        seen.add(n)
                    queue.append((n, h+1))
    return trails

@profiler
def part1(data):
    G = data
    trail_starts = [k for k, v in G.items() if v == '0']
    return sum(num_trails(s, G) for s in trail_starts)


@profiler
def part2(data):
    G = data
    trail_starts = [k for k, v in G.items() if v == '0']
    return sum(num_trails(s, G, part1=False) for s in trail_starts)

    
if __name__=='__main__':
    data = parse_input('10')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')