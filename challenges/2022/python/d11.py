'''

Advent of Code - 2022

--- Day 11: Monkey in the Middle ---

'''

from utils import *

pattern = """\
Monkey (.+):
  Starting items: (.+)
  Operation: new = old (.+) (.+)
  Test: divisible by (.+)
    If true: throw to monkey (.+)
    If false: throw to monkey (.+)"""

class Monkey:
    def __init__(self, m):
        [(id, items, op, n, test, t, f)] = re.findall(pattern, m)
        self.id = id
        self.items = digits(items)
        self.op = mul if op == '*' else add
        self.n = n
        self.test = test
        self.t = t
        self.f = f

def parse_input(day):
    return day_input(day, delimiter='\n\n', parser=Monkey)

@profiler
def part1(data, rounds=20):
    inspected = defaultdict(int)
    items = { monkey.id: monkey.items[:] for monkey in data}
    for _ in range(rounds):
        for monkey in data:
            inspected[monkey.id] += len(items[monkey.id])   # number of items processed by the monkey on this round
            while items[monkey.id]:
                item = items[monkey.id].pop(0)
                n = item if monkey.n == 'old' else int(monkey.n)
                new = monkey.op(item, n) 
                new = new // 3
                if new % int(monkey.test) == 0:
                    items[monkey.t].append(new)
                else:
                    items[monkey.f].append(new)

    #return inspected
    #return reduce(mul, sorted(inspected.values())[-2:], 1)
    return prod(sorted(inspected.values())[-2:])

@profiler
def part2(data, rounds=10_000):
    inspected = defaultdict(int)
    items = { monkey.id: monkey.items[:] for monkey in data}
    m = prod(int(monkey.test) for monkey in data)
    for _ in range(rounds):
        for monkey in data:
            inspected[monkey.id] += len(items[monkey.id])   # number of items processed by the monkey on this round
            while items[monkey.id]:
                item = items[monkey.id].pop(0)
                n = item if monkey.n == 'old' else int(monkey.n)
                new = monkey.op(item, n) % m 
                if new % int(monkey.test) == 0:
                    items[monkey.t].append(new)
                else:
                    items[monkey.f].append(new)

    return reduce(mul, sorted(inspected.values())[-2:], 1)
    
if __name__=='__main__':
    data = parse_input('11')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')