import numpy

def eval_direction(direction):
    if direction == "forward":
        return numpy.array((1, 0))
    elif direction == "up":
        return numpy.array((0, -1))
    elif direction == "down":
        return numpy.array((0, 1))

with open("python/day2/d2.txt") as f:
    starting_pos = numpy.array((0, 0))
    for line in f:
        (direction, magnitude) = line.split()
        starting_pos += eval_direction(direction) * int(magnitude)

    print(starting_pos[0] * starting_pos[1])