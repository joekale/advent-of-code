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

last_winner = np.array((5,5), dtype=np.bool) # want to learn a better way than this...
last_mark = np.array((5,5), dtype=np.bool) # want to learn a better way than this...
last_call = 0
for call in calls:
    marks |= np.where(boards == call, True, False)
    winner = [board for board, marks in zip(boards, marks) if np.any(marks.all(axis=0)) or np.any(marks.all(axis=1))]
    if len(winner) > 0:
        for win in winner:
            last_winner = win
            mask = np.where([not np.array_equal(board, win) for board in boards])
            last_mark = marks[np.where([np.array_equal(board,win) for board in boards])][0]
            marks = marks[mask]
            boards = boards[mask]
            last_call = call

print(last_winner)
print(sum(last_winner[np.where(np.invert(last_mark))]) * last_call)

# if len(winner) == 1:
#         mark_board = marks[)][0]
#         
#         break