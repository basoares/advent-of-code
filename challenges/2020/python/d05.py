'''

Advent of Code - 2020

--- Day 5: Binary Boarding  ---

'''

from utils import *

def parse_input(day):
    return day_input(day)

def part1(data):
    '''Treat the boarding pass as a binary number replacing B and R for 1 and F and L for 0
    Example:
    FBFBBFFRLR corresponds to column 44 and row 5 => 44*8+5 = 357 (seat ID)

    Replacing F|L with 0, and B|R with 1, results in 0101100101.
    The column correspond to bits 0101100, which is 44, the row corresponds to bits 101, which is 5. 
    The column must be multiplied by 8 which corresponds to a shift of 3 places (2^3 = 8) to the left (0101100000) plus the column (101)
    Resulting in 0101100101 which is 357'''

    seatIDs = [int(''.join([str(1) if l in ['B', 'R'] else str(0) for l in line]), 2) for line in data]
    return max(seatIDs)

def part12(data):
    t = str.maketrans('FBLR', '0101')
    return max(int(bp.translate(t), 2) for bp in data)

def part2(data):
    seatIDs = [int(''.join([str(1) if l in ['B', 'R'] else str(0) for l in line]), 2) for line in data]
    
    for x in range(min(seatIDs), max(seatIDs)):
        if x not in seatIDs and x-1 in seatIDs and x+1 in seatIDs:
            return x
    
if __name__ == '__main__':
    data = parse_input('05')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
