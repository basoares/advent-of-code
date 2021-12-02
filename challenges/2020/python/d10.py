'''

Advent of Code - 2020

--- Day 10: Adapter Array  ---

'''

from utils import *

def parse_input(day):
    return day_input(day, int)

def part1(data):
    adapters = sorted(data + [0])
    adapters.append(max(adapters)+3)

    diffs = Counter(b-a for a, b in zip(adapters, adapters[1:]))

    return diffs[1] * diffs[3]

def part2(data):
    adapters = sorted(data + [0])
    adapters.append(max(adapters)+3)

    paths = {}
    def possible_next_steps(i):
        if i == len(adapters) - 1:
            # there is only one step from i to the end of the of the adapter chain
            return 1
        else:
            if i in paths:
                return paths[i]

            num_paths = 0
            for j in range(i+1, len(adapters)):
                if adapters[j] - adapters[i] <= 3:
                    num_paths += possible_next_steps(j)

            paths[i] = num_paths

        return num_paths

    return possible_next_steps(0)    

if __name__ == '__main__':
    data = parse_input('10')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
