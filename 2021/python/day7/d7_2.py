import numpy as np

def eval_idx(idx, counts):
    return sum([sum([i + 1 for i in range(abs(i - idx))]) * val for i, val in enumerate(counts)])

with open("python/day7/d7.txt") as f:
    pos = np.asarray([val for val in f.readline().strip().split(',')], dtype=np.int)

max = np.max(pos)
med = int(np.median(pos))
mean = int(np.mean(pos))
print(f"max: {max}, median: {med}, mean: {mean}")

counts = np.zeros((max + 1), dtype=np.int)
for val in pos:
    counts[val] += 1

idx = mean
print(min(eval_idx(idx, counts),eval_idx(idx-1, counts), eval_idx(idx+1, counts)))
