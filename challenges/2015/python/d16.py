'''

Advent of Code - 2015

    --- Day 16: Aunt Sue ---

Released under the MIT License <http://opensource.org/licenses/mit-license.php>

'''

from re import findall
from collections import defaultdict

goal = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1        
}

def parse_input(aunts):
    res = defaultdict(dict)
    for a in aunts:
        name, details = a.split(': ', 1)    #split on first occurrence
        matches = findall(r'([a-z]+): ([0-9]{1})', details)
        res[name] = {m[0] : int(m[1]) for m in matches}

        #for d in details.split(', '):
        #    compound, num = d.split(': ')
        #    res[name][compound] = int(num)
            
    return res

def part1(details):
    aunts = parse_input(details)
    for aunt, compounds in aunts.items():
        if all(goal[k] == v for k, v in compounds.items()):
            return aunt.split()[1]

def part2(details):
    aunts = parse_input(details)
    for aunt, compounds in aunts.items():
        for k, v in compounds.items():
            if k in ['cats', 'trees']:
                if goal[k] >= v:
                    break
            elif k in ['pomeranians', 'goldfish']:
                if goal[k] <= v:
                    break
            else:
                if goal[k] != v:
                    break 
        else:    
            return aunt.split()[1]

if __name__ == '__main__':
    with open('../input/d16.txt', mode='r') as f:
        _input = f.readlines()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
