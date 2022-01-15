import numpy as np

def eval_day(arr):
    arr = np.roll(arr, -1)
    arr[6] += arr[8]
    return arr

fish = np.zeros((9), dtype=np.int)
with open("python/day6/d6.txt") as f:
    for val in f.readline().strip().split(','):
        fish[int(val)] += 1

for i in range(256):
    fish = eval_day(fish)

print(np.sum(fish))