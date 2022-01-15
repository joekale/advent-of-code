import re
points = {")": 3, "]": 57, "}":1197, ">": 25137}
pairs = {"{": "}", "(": ")", "[": "]", "<": ">"}

def find_error(line):
    open = []
    for char in line.strip():
        if char in pairs.keys():
            open.append(char)
        else:
            if pairs[open.pop()] != char:
                return char 


with open("python/day10/d10.txt") as f:
    total = 0
    for line in f:
        error = find_error(line.strip())
        if not error:
            print(f"skipping incomplete line: {line}")
        else:
            total += points[error]
            print(total)
