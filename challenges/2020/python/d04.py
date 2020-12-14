'''

Advent of Code - 2020

--- Day 4: Passport Processing  ---

'''

from utils import *

class Passport():
    def __init__(self, fields):
        self.fields = fields

    @classmethod
    def from_input(cls, data):
        instances = []
        for lines in data:
            #fields = {}
            fields = defaultdict(lambda : '0')
            for line in lines.split('\n'):
                if line:
                    for field in line.split(' '):
                        k, v = field.split(':')
                        fields[k] = v
            instances.append(cls(fields))

        return instances
    
def parse_input(day):
    raw = day_input(day, delimiter='\n\n')
    return Passport.from_input(raw)

def part1(data):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return sum(all(field in passport.fields for field in required_fields) for passport in data)

def part2(data):
    def is_valid(passport):
        return all([
                1920 <= int(passport.fields['byr']) <= 2002,
                2010 <= int(passport.fields['iyr']) <= 2020,
                2020 <= int(passport.fields['eyr']) <= 2030,
                re.match(r'^(1([5-8][0-9]|9[0-3])cm)|((59|6[0-9]|7[0-6])in)$', passport.fields['hgt']),
                re.match(r'^#[0-9a-f]{6}$', passport.fields['hcl']),
                passport.fields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
                re.match(r'^[0-9]{9}$', passport.fields['pid'])
        ])
    
    return sum(is_valid(passport) for passport in data)
    
if __name__ == '__main__':
    data = parse_input('04')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
