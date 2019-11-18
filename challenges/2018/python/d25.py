import re
from collections import defaultdict, deque

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) + abs(a[3] - b[3])

def part1(points):
    coordinates = [tuple(list(map(int, re.findall(r'-?\d+', p)))) for p in points]

    neighbours = defaultdict(list)
    for c in coordinates:
        neighbours[c] = [other for other in coordinates if manhattan_distance(c, other) <= 3 and c != other]

    constellations = []
    seen = set()
    for coord, n in neighbours.items():
        if coord in seen:
            continue

        seen.add(coord)
        constellation = [coord]
        queue = deque(n)

        while queue:
            c = queue.popleft()
            if c in seen:
                continue

            constellation.append(c)
            seen.add(c)
            queue.extendleft(neighbours[c])
        
        constellations.append(constellation)

    return len(constellations)

if __name__ == '__main__':
    with open('../input/d25.txt', mode='r') as f:
        _input = f.read().splitlines()

    print('Part One: {}'.format(part1(_input)))
