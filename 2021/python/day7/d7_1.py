import numpy as np
import math


with open("python/day7/d7.txt") as f:
    pos = np.asarray([val for val in f.readline().strip().split(',')], dtype=np.int)

max = np.max(pos)
med = int(np.median(pos))

count = np.zeros((max + 1), dtype=np.int)
for val in pos:
    count[val] += 1

print(sum([abs(i - med) * val for i, val in enumerate(count)]))