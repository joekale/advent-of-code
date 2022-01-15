import re
points = {")": 1, "]": 2, "}":3, ">": 4}
pairs = {"{": "}", "(": ")", "[": "]", "<": ">"}

def find_error(line):
    open = []
    for char in line.strip():
        if char in pairs.keys():
            open.append(char)
        else:
            if pairs[open.pop()] != char:
                return None 
    
    return open

totals = []
with open("python/day10/d10.txt") as f:
    for line in f:
        total = 0
        error = find_error(line.strip())
        if not error:
            continue
        else:
            for char in error[::-1]:
                total *= 5
                total += points[pairs[char]]

        totals.append(total)

print(sorted(totals)[len(totals)//2])