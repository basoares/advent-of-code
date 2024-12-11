'''

Advent of Code - 2024

--- Day 8: Resonant Collinearity --- 

'''

from utils import *

def parse_input(day):
    data = day_input(day)

    G = {(x, y): c for y, row in enumerate(data) for x, c in enumerate(row)}

    antennas = defaultdict(list)
    for k, v in G.items():
        if v != '.':
            antennas[v].append(k)

    return G, antennas

@profiler
def part1(data):
    G, antennas = data

    antinodes = set()
    for coords in antennas.values():
        for i, ant1 in enumerate(coords):
            for ant2 in coords[i+1:]:
                x1, y1 = ant1
                x2, y2 = ant2
                a1 = (2*x2 - x1, 2*y2 - y1)
                a2 = (2*x1 - x2, 2*y1 - y2)

                if a1 in G:
                    antinodes.add(a1)
                if a2 in G:
                    antinodes.add(a2)

    return len(antinodes)


@profiler
def part2(data):
    G, antennas = data

    antinodes = set()
    for coords in antennas.values():
        for ant1 in coords:
            for ant2 in coords:
                if ant1 == ant2: continue
                x1, y1 = ant1
                x2, y2 = ant2

                dx = x2 - x1
                dy = y2 - y1
                while (x1, y1) in G:
                    antinodes.add((x1, y1))
                    x1 += dx
                    y1 += dy

                dx = x1 - x2
                dy = y1 - y2
                while (x2, y2) in G:
                    antinodes.add((x2, y2))
                    x2 -= dx
                    y2 -= dy

    return len(antinodes)
    
if __name__=='__main__':
    data = parse_input('08')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')