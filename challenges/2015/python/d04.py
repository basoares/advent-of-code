'''

Advent of Code - 2015

--- Day 4: The Ideal Stocking Stuffer ---

'''

from hashlib import md5

def part1(key='ckczppom'):
    for i in range(1000000):
        h = md5((key + str(i)).encode()).hexdigest()
        if h[:5] == '00000':
            return i

def part2(key='ckczppom'):
    for i in range(100000000):
        h = md5((key + str(i)).encode()).hexdigest()
        if h[:6] == '000000':
            return i

if __name__ == '__main__':
    with open('../input/d04.txt', mode='r') as f:
        _input = f.read()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
