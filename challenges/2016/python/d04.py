'''

Advent of Code - 2016

--- Day 4: Security Through Obscurity ---

'''

from utils import *

def parse_input(day):
    #aaaaa-bbb-z-y-x-123[abxyz]
    parser = lambda line : re.match(r'(.+)-(\d+)\[(\w+)\]', line).groups()
    return day_input(day, parser)

@profiler
def part1(data):
    def valid_room(name, checksum):
        counts = Counter(name.replace('-', ''))
        letters = sorted(counts, key=lambda c : (-counts[c], c))
        return checksum == ''.join(letters[:5])

    return sum(int(sectorID) for name, sectorID, checksum in data if valid_room(name, checksum))

def decrypt(name, sectorID):
    decoded = ""
    shift = sectorID % 26
    for letter in name:
        if letter == '-':
            decoded += ' '
        else:
            decoded += chr(((ord(letter) - ord('a') + shift) % 26) + ord('a'))
    return decoded

@profiler
def part2(data):
    #for name, sectorID, _ in [('qzmt-zixmtkozy-ivhz', '343', '')]:
    for name, sectorID, _ in data:
        if 'north' in decrypt(name, int(sectorID)):
            return sectorID

if __name__=='__main__':
    data = parse_input('04')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')