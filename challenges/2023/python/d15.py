'''

Advent of Code - 2023

--- Day 15: Lens Library  ---

'''

from utils import *

def parse_input(day):
    return day_input(day, delimiter=',')

def hash(string):
    n = 0
    for c in string:
        n += ord(c)
        n *= 17
        n %= 256
    return n

def hash_(string):
    return reduce(lambda n, c: (n+ord(c)) * 17 % 256, string, 0)

@profiler
def part1(data):
    #return sum(hash_(step) for step in data)
    return sum(map(hash, data))

@profiler
def part2(data):
    boxes = defaultdict(list)
    for step in data:
        if '-' in step:
            lens = step[:-1]
            box = hash(lens)
            if box in boxes:
                boxes[box] = [(l, f) for (l, f) in boxes[box] if l != lens] # remove lens
        else:
            lens, focal_len = step.split('=')
            box = hash(lens)
            if box in boxes:
                if any(1 if l == lens else 0 for (l, _) in boxes[box]): #lens in box
                    boxes[box] = [(l, f) if l != lens else (l, int(focal_len)) for (l, f) in boxes[box]] # update focal length
                else:
                    boxes[box].append((lens, int(focal_len))) # add to the back of the box
            else:
                boxes[box] = [(lens, int(focal_len))]

    ans = 0
    for box, lenses in boxes.items():
        for slot, (lens, focal_len) in enumerate(lenses, 1):
            #print(lens, box, slot, focal_len, 'focusing_power --> ', (box+1) * slot * focal_len)
            ans += (box+1) * slot * focal_len 
    return ans

if __name__=='__main__':
    data = parse_input('15')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')