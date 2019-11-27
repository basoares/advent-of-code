'''

Advent of Code - 2015

    --- Day 15: Science for Hungry People ---

'''

from re import match
from collections import namedtuple
from itertools import combinations_with_replacement
from operator import mul
from functools import reduce

Ingredient = namedtuple('Ingredient', ['name', 'capacity', 'durability', 'flavor', 'texture', 'calories'])

def parse_input(ingredients):
    res = []
    for i in ingredients:
        x = match(r'(\S+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', i)
        n, cap, dur, fla, tex, cal = x.group(1, 2, 3, 4, 5, 6)
        res.append(Ingredient(n, int(cap), int(dur), int(fla), int(tex), int(cal)))

    return res

def score(recipe):
    ingredients = [sum(i) for i in list(zip(*recipe))[1:-1]] #slicing of the list to remove the "Name" of the ingredient and the "calories" 
    return reduce(mul, [i if i > 0 else 0 for i in ingredients]) #if the sum of the respective properties is negative, it becomes 0 (zero)

def part1(ingredients):
    ing = parse_input(ingredients)
    recipes = combinations_with_replacement(ing, 100)

    return max(score(r) for r in recipes)

def calories_score(recipe):
    return sum(c for c in list(zip(*recipe))[-1]) #slicing of the list to get only the "calories"

def part2(ingredients):
    ing = parse_input(ingredients)
    recipes = combinations_with_replacement(ing, 100)

    return max(score(r) for r in recipes if calories_score(r) == 500)

if __name__ == '__main__':
    with open('../input/d15.txt', mode='r') as f:
        _input = f.readlines()

        print('Part One: {}'.format(part1(_input)))
        print('Part Two: {}'.format(part2(_input)))
