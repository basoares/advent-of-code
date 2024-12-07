'''

Advent of Code - 2024

--- Day 7: Bridge Repair --- 

'''

from utils import *

def parse_input(day):
    return day_input(day, parser=integers)


def evaluate(nums, cur, target, part=1):
    if not nums:
        return cur == target
    else:
        return evaluate(nums[1:], cur * nums[0], target, part) \
            or evaluate(nums[1:], cur + nums[0], target, part) \
            or ( part==2 and evaluate(nums[1:], integer(str(cur) + str(nums[0])), target, part))


@profiler
def part1(data):
    return sum(res for res, *nums in data if evaluate(nums[1:], nums[0], res))
                    

@profiler
def part2(data):
    return sum(res for res, *nums in data if evaluate(nums[1:], nums[0], res, part=2))
        

if __name__=='__main__':
    data = parse_input('07')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')