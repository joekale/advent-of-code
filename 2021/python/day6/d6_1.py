import numpy as np

with open("python/day6/d6_sample.txt") as f:
    fish = np.asarray(f.readline().strip().split(','), dtype=np.byte)

print(len(fish))
for i in range(0,80):
    fish -= 1
    count = np.count_nonzero(fish < 0)
    if count > 0:
        new_fish = np.ones((count), dtype=np.byte) * 8
        fish = np.concatenate((fish, new_fish))
        fish[np.where(fish < 0)] = 6

print(len(fish))