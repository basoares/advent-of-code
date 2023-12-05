'''

Advent of Code - 2023

--- Day 5:  ---

'''

from utils import *

def parse_input(day):
    raw = day_input(day, delimiter='\n\n')
    seeds = [int(n) for n in raw[0].split(': ')[1].split()]
    seed_to_soil = [tuple(a.split()) for a in raw[1].split('\n') if a != 'seed-to-soil map:']
    soil_to_fertilizer = [tuple(a.split()) for a in raw[2].split('\n') if a != 'soil-to-fertilizer map:']
    fertilizer_to_water = [tuple(a.split()) for a in raw[3].split('\n') if a != 'fertilizer-to-water map:']
    water_to_light = [tuple(a.split()) for a in raw[4].split('\n') if a != 'water-to-light map:']
    light_to_temperature = [tuple(a.split()) for a in raw[5].split('\n') if a != 'light-to-temperature map:']
    temperature_to_humidity = [tuple(a.split()) for a in raw[6].split('\n') if a != 'temperature-to-humidity map:']
    humidity_to_location = [tuple(a.split()) for a in raw[7].split('\n') if a != 'humidity-to-location map:']
    return seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location

@profiler
def part1(data):
    seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = data
    min_location = 99999999999999
    for seed in seeds:
        stos = -1
        for x in seed_to_soil:
            dest, start, length = list(map(int, x))
            if seed in range(start, start+length+1):
                stos = dest + (seed - start)
                
        if stos == -1:
            stos = seed
        
        stof = -1
        for x in soil_to_fertilizer:
            dest, start, length = list(map(int, x))
            if stos in range(start, start+length+1):
                stof = dest + (stos - start)
                
        if stof == -1:
            stof = stos

        ftow = -1
        for x in fertilizer_to_water:
            dest, start, length = list(map(int, x))
            if stof in range(start, start+length+1):
                ftow = dest + (stof - start)
                
        if ftow == -1:
            ftow = stof
        
        wtol = -1
        for x in water_to_light:
            dest, start, length = list(map(int, x))
            if ftow in range(start, start+length+1):
                wtol = dest + (ftow - start)
                
        if wtol == -1:
            wtol = ftow

        ltot = -1
        for x in light_to_temperature:
            dest, start, length = list(map(int, x))
            if wtol in range(start, start+length+1):
                ltot = dest + (wtol - start)
                
        if ltot == -1:
            ltot = wtol

        ttoh = -1
        for x in temperature_to_humidity:
            dest, start, length = list(map(int, x))
            if ltot in range(start, start+length+1):
                ttoh = dest + (ltot - start)
                
        if ttoh == -1:
            ttoh = ltot

        htol = -1
        for x in humidity_to_location:
            dest, start, length = list(map(int, x))
            if ttoh in range(start, start+length+1):
                htol = dest + (ttoh - start)
                
        if htol == -1:
            htol = ttoh

        min_location = min(min_location, htol)

    return min_location

@profiler
def part2(data):
    seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = data
    min_location = 99999999999999
    seed_ranges = zip(seeds, seeds[1:])
    for sr in seed_ranges:
        srs, sre = sr
        for seed in range(srs, sre+1):
            stos = -1
            for x in seed_to_soil:
                dest, start, length = list(map(int, x))
                if seed in range(start, start+length+1):
                    stos = dest + (seed - start)
                    break
                    
            if stos == -1:
                stos = seed
            
            stof = -1
            for x in soil_to_fertilizer:
                dest, start, length = list(map(int, x))
                if stos in range(start, start+length+1):
                    stof = dest + (stos - start)
                    break
                    
            if stof == -1:
                stof = stos

            ftow = -1
            for x in fertilizer_to_water:
                dest, start, length = list(map(int, x))
                if stof in range(start, start+length+1):
                    ftow = dest + (stof - start)
                    break
                    
            if ftow == -1:
                ftow = stof
            
            wtol = -1
            for x in water_to_light:
                dest, start, length = list(map(int, x))
                if ftow in range(start, start+length+1):
                    wtol = dest + (ftow - start)
                    break
                    
            if wtol == -1:
                wtol = ftow

            ltot = -1
            for x in light_to_temperature:
                dest, start, length = list(map(int, x))
                if wtol in range(start, start+length+1):
                    ltot = dest + (wtol - start)
                    break
                    
            if ltot == -1:
                ltot = wtol

            ttoh = -1
            for x in temperature_to_humidity:
                dest, start, length = list(map(int, x))
                if ltot in range(start, start+length+1):
                    ttoh = dest + (ltot - start)
                    break
                    
            if ttoh == -1:
                ttoh = ltot

            htol = -1
            for x in humidity_to_location:
                dest, start, length = list(map(int, x))
                if ttoh in range(start, start+length+1):
                    htol = dest + (ttoh - start)
                    break
                    
            if htol == -1:
                htol = ttoh

            min_location = min(min_location, htol)

    return min_location
    
if __name__=='__main__':
    data = parse_input('05')

    print(f'Part One: {part1(data)}')
    print(f'Part Two: {part2(data)}')