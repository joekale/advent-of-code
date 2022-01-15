import numpy


with open("python/day2/d2.txt") as f:
    h = 0
    d = 0
    aim = 0
    for line in f:
        direction, magnitude = line.split()
        if direction == "forward":
            h += int(magnitude)
            d += int(magnitude) * aim
        elif direction == "up":
            aim -= int(magnitude)
        else:
            aim += int(magnitude)

    print(h * d)