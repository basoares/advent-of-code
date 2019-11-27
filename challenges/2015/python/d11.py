'''

Advent of Code - 2015

    --- Day 11: Corporate Policy ---

'''

import re

def is_valid(password):
    #all substrings of length 3
    if all(ord(s[2]) - ord(s[1]) != 1 or ord(s[1]) - ord(s[0]) != 1 for s in [password[i:i+3] for i in range(len(password)-2)]):
        return False
    #contains any of the invalid letters
    if any(password[i] in 'iol' for i in range(len(password))):
        return False
    #does not contain two pairs of letters
    if not re.search(r'([a-z])\1.*([a-z])\2', password):
        return False

    return True

def increment(password):
    if password[-1] == 'z':
        return increment(password[:-1]) + 'a'
    else:
        return password[:-1] + chr(ord(password[-1])+1)

def part1(password='cqjxjnds'):
    while not is_valid(password):
        password = increment(password)

    return password

def part2(password='cqjxjnds'):
    p = part1(password)
    p = increment(p)
    while not is_valid(p):
        p = increment(p)

    return p

if __name__ == '__main__':
    with open('../input/d11.txt', mode='r') as f:
        _input = f.readline()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
