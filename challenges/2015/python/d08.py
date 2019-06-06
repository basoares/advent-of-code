'''

Advent of Code - 2015

    --- Day 8: Matchsticks ---

Released under the MIT License <http://opensource.org/licenses/mit-license.php>

'''

import re

def part1(text):
    return sum(len(line.strip()) - len(eval(line.strip())) for line in text)

def part2(text):
    regexp = re.compile(r'("|\\x\d{2}|\\)')
    return sum(len('"' + regexp.sub(r'\\\1', line.strip()) + '"') - len(line.strip()) for line in text)

if __name__ == '__main__':
    with open('../input/d08.txt', mode='r') as f:
        _input = f.readlines()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
