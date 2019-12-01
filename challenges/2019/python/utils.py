'''
    Imports and utility functions 
'''
#region Imports

import os, sys

import re
from collections import defaultdict, Counter, deque, namedtuple
from itertools import chain, combinations, product
from copy import deepcopy

#endregion

#region FileInput

def day_input(day, parser=str.strip, fpath='../input/d{}.txt'):
    with open(fpath.format(day)) as f:
        return [parser(l) for l in f]

#endregion

#region Utilities

def fst(x):
    '''First element of a pair'''
    return x[0]

def snd(x):
    '''Second element of a pair'''
    return x[1]

def neighbors4(point):
    '''The four neighboring squares'''
    x, y = point
    return [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]

def neighbors8(point):
    '''The eight neighboring squares'''
    x, y = point
    return [(x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1),
            (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1)]

def distance(a, b): 
    "Straightline distance between two points."
    return ( ((fst(a)-fst(b)) ** 2) + ((snd(a)-snd(b)) ** 2) ) ** 0.5

def manhattan_distance(a, b):
    return abs(fst(a) - fst(b)) + abs(snd(a) - snd(b))

#endregion

#region Lists

def integers(line):
    return [int(i) for i in re.findall(r'-?\d+', line)]

def flatten(l):
    return [e for x in l for e in x]

#endregion

