'''
    Imports and utility functions 
'''
#region Imports

import os, sys

import re
from collections import defaultdict, Counter, deque, namedtuple
from itertools import chain, combinations, product, permutations, cycle, count
from copy import deepcopy
from math import gcd, sqrt, atan2, degrees, ceil, floor
from networkx import Graph, DiGraph, all_pairs_shortest_path, transitive_closure, shortest_path_length
import time
import hashlib
import string

#endregion

#region FileInput

#def day_input(day, parser=str.strip, fpath='../input/d{}.txt'):
#    with open(fpath.format(day)) as f:
#        return [parser(l) for l in f]

def day_input(day, parser=str.strip, delimiter='\n', fpath='../input/d{}.txt'):
    with open(fpath.format(day)) as f:
        return [parser(l) for l in f.read().split(delimiter)]

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

def lcm(x, y):
    return x // gcd(x, y) * y

#endregion

#region Lists

def integers(line):
    return [int(i) for i in re.findall(r'-?\d+', line)]

def flatten(l):
    return [e for x in l for e in x]

class DynamicList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setitem__(self, index, item):
        self.expand(index)
        return super().__setitem__(index, item)

    def __getitem__(self, index):
        self.expand(index)
        return super().__getitem__(index)
    
    def expand(self, index):
        if isinstance(index, int):
            index += 1
        elif isinstance(index, slice):
            if isinstance(index.start, int) or isinstance(index.stop, int):
                index = max(index.start, index.stop)

        if isinstance(index, int) and index >= len(self):
            self.extend([0] * (index - len(self)))

#endregion

def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' +
              "{:2.5f}".format(time.time()-t) + ' sec')
        return ret
    return wrapper_method