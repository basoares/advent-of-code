'''

Advent of Code - 2015

--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Released under the MIT License <http://opensource.org/licenses/mit-license.php>

'''

import re
from collections import defaultdict

def update_position(pos, m):
    return {'^': (pos[0], pos[1]+1), 
            'v': (pos[0], pos[1]-1), 
            '<': (pos[0]-1, pos[1]), 
            '>': (pos[0]+1, pos[1])
           }[m]

def part1(moves):
    current_location = (0, 0)
    visited_houses = set([current_location])

    for m in moves:
        current_location = update_position(current_location, m)
        visited_houses.add(current_location)

    return len(visited_houses)

def part2(moves):
    current_locations = [(0, 0), (0, 0)]
    visited_houses = set([(0, 0)])

    for i, m in enumerate(moves):
        house = current_locations[i%2] = update_position(current_locations[i%2], m)
        visited_houses.add(house)

    return len(visited_houses)

if __name__ == '__main__':
    with open('../input/d03.txt', mode='r') as f:
        _input = f.readline()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
