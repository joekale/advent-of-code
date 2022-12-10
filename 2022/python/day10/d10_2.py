import logging
import re
import matplotlib.pyplot as plt
from typing import Tuple

logging.basicConfig(level=logging.DEBUG)

_NOOP = re.compile(r"noop")
_ADDX = re.compile(r"addx\s(-?\d+)")

def read_instruction(line):
    if _NOOP.match(line):
        return (1, 0)
    if _ADDX.match(line):
        modifier = _ADDX.findall(line)
        return (2, int(modifier[0]))

answer = 0
check_interval = [40, 80, 120, 160, 200, 240]
screen = []
current_row = 0
logging.debug(screen)
with open("input.txt", "r") as f:
    cycle = 0
    x = 1
    for line in f:
        (cycle_inc, modifier) = read_instruction(line.strip())
        for i in range(cycle_inc):
            cycle += 1
            if (cycle - 1) % 40 in [x - 1, x, x + 1]:
                screen.append((((cycle - 1) % 40), 6 - current_row))
            if cycle in check_interval:
                current_row += 1
        
        x += modifier

fig, ax = plt.subplots(figsize=(10, 6))
r1, r2 = map(list, zip(*screen))
ax.scatter(x=r1, y=r2)
plt.show()
logging.info(f"answer = \n{screen}")

