'''

Advent of Code - 2021

--- Day 12: Passage Pathing ---

'''

from utils import *

def parse_input(day):
    parser = lambda line: line.split('-')
    raw = day_input(day, parser)

    caves = defaultdict(list)
    for a, b in raw:
        caves[a].append(b)
        caves[b].append(a)

    return caves


def in_path(cave, path):
    return any(c[0] == cave for c in path)


@profiler
def part1(data):
    paths = []
    queue = deque([[('start', 0)]])
    while queue:
        path = queue.popleft()
        last_cave, distance = path[-1]

        for adj in data[last_cave]: #caves adjacent to the last cave in the path
            if adj == 'end':
                paths.append(path + [(adj, distance+1)])
            elif not adj.islower() or not in_path(adj, path):
                queue.append(path + [(adj, distance+1)])
                
    return len(paths)

                
@profiler
def part2(data):
    paths = []
    queue = deque([[('start', False)]])
    while queue:
        path = queue.popleft()
        last_cave, dupe = path[-1]

        for adj in data[last_cave]: #caves adjacent to the last cave in the path
            if adj == 'start':
                continue
            elif adj == 'end':
                paths.append(path + [(adj, dupe)])
            elif not adj.islower() or not in_path(adj, path) or not dupe:
                if in_path(adj, path) and adj.islower():
                    queue.append(path + [(adj, True)])
                else:
                    queue.append(path + [(adj, dupe)])
                
    return len(paths)


if __name__=='__main__':
    data = parse_input('12')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')