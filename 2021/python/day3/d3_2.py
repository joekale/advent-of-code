import numpy

def line_to_int(line):
    return sum([bit * (2 ** (len(line) - i - 1)) for i, bit in enumerate(line)])

def filter_list(lines, pos, most):
    bit_positions = sum(lines, numpy.zeros((lines.shape[1]), dtype=numpy.int))
    common = most if len(lines) / bit_positions[pos] <= 2 else not most
    return [line for line in lines if line[pos] == common]

def get(lines, oxygen):
    bit = 0
    while(True):
        lines = numpy.asarray(filter_list(lines, bit, oxygen))
        if len(lines) == 1:
            return lines[0]
        bit += 1

lines = list()

with open("python/day3/d3.txt") as f:
    for line in f:
        lines.append(numpy.asarray(list(line.strip()), dtype=numpy.int))

lines = numpy.asarray(lines)

oxygen = line_to_int(get(lines, True))
co2 = line_to_int(get(lines, False))
print(f"oxygen: {oxygen}, co2: {co2}, life_support: {oxygen * co2}")
