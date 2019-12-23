'''

Advent of Code - 2019

--- Day 12: The N-Body Problem ---

'''

from utils import *

class Moon():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vx = 0
        self.vy = 0
        self.vz = 0

    def step(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.z = self.z + self.vz

    def total_energy(self):
        return (abs(self.x)+abs(self.y)+abs(self.z)) * (abs(self.vx)+abs(self.vy)+abs(self.vz))

    def __str__(self):
        return f'<x={self.x}, y={self.y}, z={self.z}>'

def parse_input(day):
    moons = day_input(day, integers)

    return [Moon(int(x), int(y), int(z)) for x, y, z in moons]

def part1(moons):
    for _ in range(1000):
        for m1, m2 in combinations(moons, 2):
            if m1.x != m2.x:
                m1.vx += 1 if m2.x > m1.x else -1
                m2.vx += 1 if m1.x > m2.x else -1 
            if m1.y != m2.y:
                m1.vy += 1 if m2.y > m1.y else -1
                m2.vy += 1 if m1.y > m2.y else -1 
            if m1.z != m2.z:
                m1.vz += 1 if m2.z > m1.z else -1
                m2.vz += 1 if m1.z > m2.z else -1 

        for m in moons:
            m.step()

    return sum(m.total_energy() for m in moons)

def part2(moons):
    i = 0
    
    start_x = str([(m.x, m.vx) for m in moons])    
    repx = 0
    start_y = str([(m.y, m.vy) for m in moons])    
    repy = 0
    start_z = str([(m.z, m.vz) for m in moons])    
    repz = 0
   
    while True:
        for m1, m2 in combinations(moons, 2):
            if m1.x != m2.x:
                m1.vx += 1 if m2.x > m1.x else -1
                m2.vx += 1 if m1.x > m2.x else -1 
            if m1.y != m2.y:
                m1.vy += 1 if m2.y > m1.y else -1
                m2.vy += 1 if m1.y > m2.y else -1 
            if m1.z != m2.z:
                m1.vz += 1 if m2.z > m1.z else -1
                m2.vz += 1 if m1.z > m2.z else -1 

        for m in moons:
            m.step()
        
        i += 1

        if repx and repy and repz:
            break  

        if start_x == str([(m.x, m.vx) for m in moons]):
            repx = i
        if start_y == str([(m.y, m.vy) for m in moons]):
            repy = i
        if start_z == str([(m.z, m.vz) for m in moons]):
            repz = i
    
    return lcm(repx, lcm(repy, repz))

if __name__ == '__main__':
    data = parse_input('12')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')
