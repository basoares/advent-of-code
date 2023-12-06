'''

Advent of Code - 2023

--- Day 4: Scratchcards  ---

'''

from utils import *

def parse_input(day):
    raw = day_input(day)
    games = []
    for game in raw:
        card, rest = game.split(': ')
        card = int(card.split()[1])
        win, other = rest.split('|')
        games.append((card, list(map(int, win.split())), list(map(int, other.split()))))
    return games
        
@profiler
def part1(data):
    ans = 0
    for _, win, other in data:
        #n = len(set(win).intersection(other))
        n = sum([o in win for o in other])
        ans += 2**(n-1) if n else 0
    return ans

@profiler
def part2(data):
    N = defaultdict(int)
    for card, win, other in data:
        N[card] += 1
        n = sum([o in win for o in other])
        for i in range(n):
            N[card+1+i] += N[card]

    return sum(N.values())
    
if __name__=='__main__':
    data = parse_input('04')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')