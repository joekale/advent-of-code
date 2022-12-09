import logging
import re

logging.basicConfig(level=logging.DEBUG)

def check_visible(x, y, grid):
    logging.debug(f"Checking ({x},{y}), height: {grid[y][x]}")
    top_visible = True
    bottom_visible = True
    left_visible = True
    right_visible = True
    for top in range(y)[::-1]:
        
        if grid[top][x] >= grid[y][x]:
            top_visible = False
    
    for bottom in range(y+1, len(grid)):
        if grid[bottom][x] >= grid[y][x]:
            bottom_visible = False
    
    for left in range(x)[::-1]:
        if grid[y][left] >= grid[y][x]:
            left_visible = False
    
    for right in range(x+1, len(grid[0])):
        if grid[y][right] >= grid[y][x]:
            right_visible = False
    
    logging.debug(f"visible from top: {top_visible}, bottom: {bottom_visible}, left: {left_visible}, right: {right_visible}")
    return top_visible or bottom_visible or left_visible or right_visible

answer = 0
grid = []
with open("input.txt", "r") as f:
    for row in f:
        if row.strip() != '':
            grid.append([int(x) for x in row.strip()])

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if check_visible(j, i, grid):
            answer += 1

logging.debug(f"internal tree visible count: {answer}.")
answer += ((len(grid) - 1) * 2) + ((len(grid[0]) - 1) * 2)

logging.info(f"answer = {answer}")

