import numpy as np

def is_min(heightmap, row, column):
    min = True
    min &= True if column == heightmap.shape[1] - 1 else (heightmap[row,column] < heightmap[row,column+1])
    min &= True if row == heightmap.shape[0] - 1 else heightmap[row,column] < heightmap[row+1, column]
    min &= True if row == 0 else heightmap[row,column] < heightmap[row-1, column]
    min &= True if column == 0 else heightmap[row,column] < heightmap[row, column-1]
    return min

with open("python/day9/d9.txt") as f:
    heightmap = np.asarray([np.asarray([int(char) for char in line.strip()]) for line in f])

mask = np.asarray([is_min(heightmap, row, column) for row in range(heightmap.shape[0]) for column in range(heightmap.shape[1])])
mask = np.reshape(mask, heightmap.shape)   
        
print(np.sum(heightmap[mask] + 1))