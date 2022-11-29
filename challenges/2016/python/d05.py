'''

Advent of Code - 2016

--- Day 5: How About a Nice Game of Chess ---

'''

from utils import *

def parse_input(day):
    return day_input(day)[0]

@profiler
def part1(data):
    password = ""
    idx = 0
    while len(password) < 8:
        hash = hashlib.md5((data + str(idx)).encode()).hexdigest()
        if hash[:5] == '00000':
            password += hash[5]
        idx += 1

    return password

@profiler
def part2(data):
    password = ['*'] * 8
    idx = 0
    while '*' in password:
        hash = hashlib.md5((data + str(idx)).encode()).hexdigest()
        if hash[:5] == '00000':
            if int(hash[5], 16) < 8 and password[int(hash[5])] == '*':
                password[int(hash[5])] = hash[6]
        idx += 1
    
    return ''.join(password)

if __name__=='__main__':
    data = parse_input('05')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')