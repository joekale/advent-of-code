import numpy as np

def boards_generator(file):
    line = f.readline()
    while len(line) > 0:
        line = line.strip()
        if len(line) == 0:
            yield np.asarray([np.asarray(f.readline().strip().split(), dtype=np.int) for i in range(0, 5)])
            line = f.readline()

with open("python/day4/d4.txt") as f:
    calls = np.asarray(f.readline().strip().split(','), dtype=np.int)
    boards = np.asarray([i for i in boards_generator(f)])

marks = np.asarray(list(), dtype=np.bool) # want to learn a better way than this...
marks = np.resize(marks, boards.shape)
for call in calls:
    marks |= np.where(boards == call, True, False)
    winner = [board for board, marks in zip(boards, marks) if np.any(marks.all(axis=0)) or np.any(marks.all(axis=1))]
    if len(winner) == 1:
        mark_board = marks[np.where([np.array_equal(board, winner[0]) for board in boards])][0]
        print(sum(winner[0][np.where(np.invert(mark_board))]) * call)
        break
