import numpy

bit_positions = numpy.zeros((10), dtype=numpy.int)
check_size = True
line_count = 0

with open("python/day3/d3.txt") as f:
    for line in f:
        line_count += 1
        if check_size and len(bit_positions) != len(line):
            check_size = False
            print(f"resizing array to {(len(line) - 1)}")
            bit_positions = numpy.resize(bit_positions, (len(line) - 1))
        
        bits = numpy.asarray(list(line.strip()), dtype=numpy.int)
        bit_positions += bits

gamma = 0
for i, bit in enumerate(bit_positions):
    if line_count / bit < 2:
        gamma += 2 ** (len(bit_positions) - i - 1)

epsilon = ~gamma & ((1 << len(bit_positions)) - 1)
print(f"gamma: {gamma}, epsilon: {epsilon}, power: {gamma * epsilon}")