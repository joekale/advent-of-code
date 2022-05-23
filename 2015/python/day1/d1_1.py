from pathlib import Path

with open(Path("2015/inputs/1.txt").resolve().as_posix()) as f:
    for line in f:
        floor = 0
        for i,char in enumerate(line):
            floor = floor + 1 if char == '(' else floor - 1
        
        print(floor)