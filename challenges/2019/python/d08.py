'''

Advent of Code - 2019

--- Day 8: Space Image Format ---

'''

from utils import *

def parse_input(day):
    return day_input(day)[0]

def part1(image, w=25, h=6):
    assert len(image) % (w*h) == 0 #verify transferred image has correct dimensions

    layers = []
    while image:
        layers.append(image[:w*h])
        image = image[w*h:]        

    best = min(layers, key = lambda l: l.count('0'))
    return best.count('1') * best.count('2')

def part2(image, w=25, h=6):
    assert len(image) % (w*h) == 0 #verify transferred image has correct dimensions

    result = image[:w*h]     #first layer
    image = image[w*h:]      #remaining layers  
    
    while image:
        aux = ''
        for r, i in zip(result, image):
            if r == '2':
                aux += i
            else:
                aux += r

        result = aux
        image = image[w*h:]

    for i in range(h):
        print(result[i*25:(i+1)*25].replace('0', ' '))

if __name__ == '__main__':
    data = parse_input('08')

    print(f'Part One: {part1(data)}')
    print('Part Two:')
    part2(data)
