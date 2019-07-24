'''

Advent of Code - 2015

    --- Day 14: Reindeer Olympics ---

Released under the MIT License <http://opensource.org/licenses/mit-license.php>

'''

from re import findall, match
from collections import defaultdict, namedtuple

Reindeer = namedtuple('Reindeer', ['name', 'speed', 'flight_time', 'rest_time'])

def parse_input(reindeers):
    rs = []
    for r in reindeers:
        x = match(r'(\S+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.', r)
        r, s, t, rest = x.group(1, 2, 3, 4)
        rs.append(Reindeer(r, int(s), int(t), int(rest)))

    return rs

def flight_distance(reindeer, t):
    cycle_length = reindeer.flight_time + reindeer.rest_time
    cycles_completed = t // cycle_length

    return (cycles_completed * reindeer.flight_time + min(reindeer.flight_time, t % cycle_length)) * reindeer.speed
    
def part1(reindeers, time=2503):
    rs = parse_input(reindeers)

    distance = defaultdict(int)
    for r in rs:
         distance[r.name] = flight_distance(r, time)

    return max(distance.values())

def part2(reindeers, time=2503):
    rs = parse_input(reindeers)

    points = defaultdict(int)
    for t in range(1, time+1):
        distances = [(r.name, flight_distance(r, t)) for r in rs]
        max_distance = max(distances, key=lambda item: item[1])[1]

        #attribute points to all the reindeers that have traveled the maximum distance at point in time t
        for (r, d) in distances:
            points[r] += 1 if d == max_distance else 0

    return max(points.values())

if __name__ == '__main__':
    with open('../input/d14.txt', mode='r') as f:
        _input = f.readlines()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
