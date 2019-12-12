'''

Advent of Code - 2019

--- Day 6: Universal Orbit Map ---

'''

from utils import *

def parse_input(day):
    parser = lambda line : tuple(line.strip().split(')'))
    return day_input(day, parser)

def num_children(n, nodes):
    if n not in nodes:
        return 0
    return len(nodes[n]) + sum(num_children(c, nodes) for c in nodes[n])

def part1(orbits):
    G = defaultdict(list)
    for a, b in orbits:
        G[a].append(b)

    total = 0
    for node in G:
        total += num_children(node, G)

    return total

def part1b(orbits):
    '''Using networkx library and calculating the transitive closure of the graph
    that represents the orbits between the different objects
    '''
    G = DiGraph()
    G.add_edges_from(orbits)
    
    return transitive_closure(G).size()


def bfs(G, start_v):
    queue = deque()         #working queue
    queue.append((start_v, 0))
    seen = {}               #Visited nodes
    while queue:
        node, depth = queue.popleft()
        seen[node] = depth
        queue.extend((v, depth+1) for v in G[node] if v not in seen)
        yield node, depth

def part2(orbits):
    G = defaultdict(list)
    for a, b in orbits:
        G[a].append(b)
        G[b].append(a)

    return next(depth - 2 for node, depth in bfs(G, 'YOU') if node == 'SAN')

def part2b(orbits):
    '''Using networkx library and calculating the shortest path between YOU and SAN'''
    G = Graph()
    G.add_edges_from(orbits)

    return shortest_path_length(G, 'YOU', 'SAN') - 2

if __name__ == '__main__':
    data = parse_input('06')

    print(f'Part One: {part1(data)}')
    #print(f'Part One: {part1b(data)}')
    print(f'Part Two: {part2(data)}')
    #print(f'Part Two: {part2b(data)}')
