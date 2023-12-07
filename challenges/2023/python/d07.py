'''

Advent of Code - 2023

--- Day 7: Camel Cards ---

'''

from utils import *

def parse_input(day):
    parser = lambda line: tuple(line.split())
    return day_input(day, parser)

def rank(hand, original_hand, ranks):
    counts = tuple(sorted(Counter(hand).values()))
    # rank is the type (5 of a kind, 4 of a kind, full house, ...) + "value" of each card in the provided order
    if counts == (5,):
        return 70_000_000_000 + int(''.join(ranks[card] for card in original_hand))
    if counts == (1, 4):
        return 60_000_000_000 + int(''.join(ranks[card] for card in original_hand))
    if counts == (2, 3):
        return 50_000_000_000 + int(''.join(ranks[card] for card in original_hand))
    if counts == (1, 1, 3):
        return 40_000_000_000 + int(''.join(ranks[card] for card in original_hand))
    if counts == (1, 2, 2):
        return 30_000_000_000 + int(''.join(ranks[card] for card in original_hand))
    if counts == (1, 1, 1, 2):
        return 20_000_000_000 + int(''.join(ranks[card] for card in original_hand))
    else:
        return 10_000_000_000 + int(''.join(ranks[card] for card in original_hand))

@profiler
def part1(data):
    ranks = {'A': '13', 'K': '12', 'Q': '11', 'J': '10', 'T': '09', '9': '08', '8': '07', '7': '06', '6': '05', '5': '04', '4': '03', '3': '02', '2': '01'}
    hands = sorted(data, key=lambda x: rank(x[0], x[0], ranks))
    return sum(int(bid)*(i+1) for i, (_, bid) in enumerate(hands))

@profiler
def part2(data):
    ranks = {'A': '13', 'K': '12', 'Q': '11', 'J': '00', 'T': '09', '9': '08', '8': '07', '7': '06', '6': '05', '5': '04', '4': '03', '3': '02', '2': '01'}
    hands = []
    for hand in data:
        m = 0
        for card in '23456789TQKA':
            m = max(m, rank(hand[0].replace('J', card), hand[0], ranks))
        hands.append((m, hand))
    hands = sorted(hands)
    return sum(int(hand[1])*(i+1) for i, (_, hand) in enumerate(hands))
    
if __name__=='__main__':
    data = parse_input('07')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')