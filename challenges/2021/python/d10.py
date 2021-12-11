'''

Advent of Code - 2021

--- Day 10: Syntax Scoring ---

'''

from utils import *

def parse_input(day):
    return day_input(day)


pairs = { ')': '(', ']': '[', '}': '{', '>': '<' }

@profiler
def part1(data):
    points = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
    score = 0
    for line in data:
        q = deque()
        for c in line:
            if c in pairs.values():
                q.append(c)
            elif not q or q.pop() != pairs[c]:
                score += points[c]
                break

    return score


@profiler
def part2(data):
    scores = []
    points = {'(': 1, '[': 2, '{': 3, '<': 4}

    for line in data:
        q = deque()
        for c in line:
            if c in pairs.values():
                q.appendleft(c)
            elif not q or q.popleft() != pairs[c]:
                q = None #corrupted
                break

        # if not corrupted
        if q:
            score = 0
            for m in q:
                score = score*5 + points[m]
            scores.append(score)

    scores = sorted(scores)
    return scores[len(scores)//2]


if __name__=='__main__':
    data = parse_input('10')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')