'''

Advent of Code - 2024

--- Day 5: Print Queue --- 

'''

from utils import *

def parse_input(day):
    _rules, _updates = day_input(day, delimiter='\n\n')

    rules = defaultdict(list)
    for pred, succ in [integers(r) for r in _rules.splitlines()]:
        rules[succ].append(pred)

    updates = [integers(u) for u in _updates.splitlines()]
    return rules, updates


def correct_order(update, rules):
    for i, page in enumerate(update):
        if page in rules:
            # correct order if none of the dependencies appears after
            if any(d in update[i+1:] for d in rules[page]):
                return False
    else:
        return True

@profiler
def part1(data):
    rules, updates = data
    
    total = 0
    for update in updates:
        if correct_order(update, rules):
            total += update[len(update) // 2]

    return total


@profiler
def part2(data):
    rules, updates = data

    def cmp(p1, p2):
        if not p1 in rules:
            return 0
        elif p2 in rules[p1]:
            return 1
        else:
            return -1

    total = 0
    for update in updates:
        if not correct_order(update, rules):
            update.sort(key=cmp_to_key(cmp))
            total += update[len(update) // 2]

    return total
    

    
if __name__=='__main__':
    data = parse_input('05')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')