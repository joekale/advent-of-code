import numpy as np
import math

def parse_coordinates(file):
    for line in file:
        coord_splits = line.split()
        yield int(coord_splits[0].split(',')[0]), int(coord_splits[0].split(',')[1]), int(coord_splits[2].split(',')[0]), int(coord_splits[2].split(',')[1])

mark_board = np.zeros((1000, 1000), dtype=np.int)

with open("python/day5/d5.txt") as f:
    for x1, y1, x2, y2 in parse_coordinates(f):
        if x1 == x2 or y1 == y2:
            mark_board[min(x1,x2):max(x1,x2)+1,min(y1,y2):max(y1,y2)+1] += 1
        else:
            view = mark_board[min(x1,x2):max(x1,x2)+1,min(y1,y2):max(y1,y2)+1]
            diag = np.diag_indices(view.shape[0])
            if x1 > x2:
                view = np.fliplr(view)
            if y1 > y2:
                view = np.flipud(view)
            view[diag] += 1

    print(len(np.extract(mark_board >= 2, mark_board)))