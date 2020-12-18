'''

Advent of Code - 2020

--- Day 6: Custom Customs  ---

'''

from utils import *

def parse_input(day):
    return day_input(day, delimiter='\n\n')

def part1(data):
    # using a set to store all the answers for each of the groups, the result consists of the sum of size of each of the sets
    yeses = 0
    for group in data:
        yeses += len({a for answers in group.split('\n') for a in answers.strip()})
        
    return yeses

def part2(data):
    # for each group, save the individual answers in a set
    # the number of questions to which everyone answered "yes" corresponds to the intersection of the different sets in the group
    yeses = 0
    for group in data:
        answers = [{a for a in answers.strip()} for answers in group.split('\n')]
        yeses += len(set.intersection(*answers))

    return yeses
    
if __name__ == '__main__':
    data = parse_input('06')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
