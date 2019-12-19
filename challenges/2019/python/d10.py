'''

Advent of Code - 2019

--- Day 10: Monitoring Station ---

'''

from utils import *
from math import gcd, sqrt, atan2, degrees

Asteroid = namedtuple('Asteroid', ['x', 'y'])

def parse_input(day):
    region = day_input(day, lambda line: line.strip())

    return [Asteroid(x, y) for y, row in enumerate(region) for x, column in enumerate(row) if column == '#']

def angle(station, asteroid):
    dx = asteroid[0]-station[0]
    dy = asteroid[1]-station[1]

    return (degrees(atan2(dy, dx))+90)%360

def asteroids_visible(station, asteroids):
    '''The number of asteroids visible corresponds to the number of distinct angles. If the angle between 
    (station, a) and (station, b) is the same, then a and b are on the same line segment, therefore 
    a is hidding b or vice versa'''
    angles = set()
    for a in asteroids:
        if a != station:
            angles.add(angle(station, a))

    return len(angles)

def part1(asteroids):
    results = [(asteroid, asteroids_visible(asteroid, asteroids)) for asteroid in asteroids]
    return max(results, key=lambda x: x[1])

def asteroids_per_angle(station, asteroids):
    g = defaultdict(list)
    for asteroid in asteroids:
        if asteroid != station:
            d = distance(station, asteroid)
            a = angle(station, asteroid)
            g[a].append((asteroid, d))
    return g

def part2(asteroids, station=Asteroid(26, 29)):
    d = asteroids_per_angle(station, asteroids)
    angles = sorted(d.keys(), reverse=False)
    
    result = []

    #sort asteroids according to distance from station
    for angle in angles:
        d[angle].sort(key=lambda x: x[1])
    
    while angles:
        for a in angles:
            if d[a]:
                result.append(d[a].pop(0))
            else:
                angles.remove(a)

    return result[199][0].x*100+result[199][0].y

if __name__ == '__main__':
    data = parse_input('10')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
