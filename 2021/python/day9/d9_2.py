import numpy as np
import math

def is_min(heightmap, row, column):
    min = True
    min &= True if column == heightmap.shape[1] - 1 else (heightmap[row,column] < heightmap[row,column+1])
    min &= True if row == heightmap.shape[0] - 1 else heightmap[row,column] < heightmap[row+1, column]
    min &= True if row == 0 else heightmap[row,column] < heightmap[row-1, column]
    min &= True if column == 0 else heightmap[row,column] < heightmap[row, column-1]
    return min

def climb_basin(heightmap, basin, index):
    if index[0] != 0 and heightmap[index[0] - 1, index[1]] != 9 and heightmap[index[0] - 1, index[1]] >= heightmap[index]:
        if (index[0] - 1, index[1]) not in basin:
            basin.append((index[0] - 1, index[1])) 
            basin = climb_basin(heightmap, basin, (index[0] - 1, index[1]))  
    if index[1] != 0 and heightmap[index[0], index[1] - 1] != 9 and heightmap[index[0], index[1] - 1] >= heightmap[index]:
        if (index[0], index[1] - 1) not in basin:
            basin.append((index[0], index[1] - 1))
            basin = climb_basin(heightmap, basin, (index[0], index[1] - 1))  
    if index[0] < heightmap.shape[0] - 1 and heightmap[index[0] + 1, index[1]] != 9 and heightmap[index[0] + 1, index[1]] >= heightmap[index]:
        if (index[0] + 1, index[1]) not in basin:
            basin.append((index[0] + 1, index[1]))
            basin = climb_basin(heightmap, basin, (index[0] + 1, index[1])) 
    if index[1] < heightmap.shape[1] - 1 and heightmap[index[0], index[1] + 1] != 9 and heightmap[index[0], index[1] + 1] >= heightmap[index]:
        if (index[0], index[1] + 1) not in basin:
            basin.append((index[0], index[1] + 1))
            basin = climb_basin(heightmap, basin, (index[0], index[1] + 1)) 
    return basin

with open("python/day9/d9.txt") as f:
    heightmap = np.asarray([np.asarray([int(char) for char in line.strip()]) for line in f])

mask = np.asarray([is_min(heightmap, row, column) for row in range(heightmap.shape[0]) for column in range(heightmap.shape[1])])
mask = np.reshape(mask, heightmap.shape)
indices = np.where(mask)

values = []        
for x,y in zip(indices[0],indices[1]):
    basin = list([(x,y)])
    basin = climb_basin(heightmap, basin, (x,y))
    values.append(len(basin))
 
print(math.prod(sorted(values)[-3:]))