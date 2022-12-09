import logging
import re

logging.basicConfig(level=logging.DEBUG)

def check_visible(x, y, grid):
    logging.debug(f"Checking ({x},{y}), height: {grid[y][x]}")
    top_distance = 0
    bottom_distance = 0
    left_distance = 0
    right_distance = 0
    for top in range(y)[::-1]:
        if grid[top][x] >= grid[y][x]:
            top_distance = y - top
            break
    
    for bottom in range(y+1, len(grid)):
        if grid[bottom][x] >= grid[y][x]:
            bottom_distance = bottom - y
            break
    
    for left in range(x)[::-1]:
        if grid[y][left] >= grid[y][x]:
            left_distance = x - left
            break
    
    for right in range(x+1, len(grid[0])):
        if grid[y][right] >= grid[y][x]:
            right_distance = right - x
            break
    
    if not right_distance:
        right_distance = len(grid[0]) - 1 - x
    if not left_distance:
        left_distance = x
    if not top_distance:
        top_distance = y
    if not bottom_distance:
        bottom_distance = len(grid) - 1 - y
    
    logging.debug(f"distance from top: {top_distance}, bottom: {bottom_distance}, left: {left_distance}, right: {right_distance}")
    return top_distance * bottom_distance * left_distance * right_distance

answer = 0
grid = []
with open("input.txt", "r") as f:
    for row in f:
        if row.strip() != '':
            grid.append([int(x) for x in row.strip()])

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        view_score = check_visible(j, i, grid)
        if view_score > answer:
            answer = view_score

# logging.debug(f"internal tree visible count: {answer}.")
# answer += ((len(grid) - 1) * 2) + ((len(grid[0]) - 1) * 2)

logging.info(f"answer = {answer}")

