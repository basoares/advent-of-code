'''

Advent of Code - 2021

--- Day 4: Giant Squid ---

'''

from utils import *

class BingoCard():
    def __init__(self, board, size=5):
        self.size = size
        self.board = board

    def set(self, draw):
        if draw in self.board:
            self.board[draw] = 1

    def bingo(self):
        rows = [list(self.board.values())[x:x+5] for x in range(0, self.size*self.size, self.size)]
        for i in range(self.size):
            if all(row[i] == 1 for row in rows) or all(r == 1 for r in rows[i]):
                return True
        return False

    def score(self):
        return sum(k for k, v in self.board.items() if v == 0)

    @classmethod
    def from_input(cls, data):
        instances = []
        for lines in data:
            board = defaultdict(lambda : 0)
            for line in lines.split('\n'):
                if line:
                    for v in re.findall(r'\d+', line):
                        board[int(v)] = 0
            instances.append(cls(board))

        return instances

def reset_cards(cards):
    for card in cards:
        card.reset()

def parse_input(day):
    draw, *cards = day_input(day, delimiter='\n\n')
    return map(int, draw.split(',')), BingoCard.from_input(cards)

    #raw = day_input(day, delimiter='\n\n')
    #draw = map(int, raw[0].split(','))
    #return draw, BingoCard.from_input(raw[1:])

@profiler
def part1(data):
    draw, cards = data

    for d in draw:
        for card in cards:
            card.set(d)
            if card.bingo():
                return card.score() * d

    raise RuntimeError(f'No winners')

@profiler
def part2(data):
    draw, cards = data
    
    completed_scores = []
    for d in draw:
        for card in cards[:]:   # COPY OF THE LIST so we can remove the complete cards below
            card.set(d)
            if card.bingo():
                completed_scores.append(card.score() * d)
                cards.remove(card)

    return completed_scores[-1]

if __name__=='__main__':
    data = parse_input('04')

    print(f'Part One: {part1(data)}')

    # because the status of the bingo cards is changed, we reload the data for part2
    data = parse_input('04')
    print(f'Part Two: {part2(data)}')