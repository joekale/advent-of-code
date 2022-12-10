import logging
import re
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
check_interval = [20, 60, 100, 140, 180, 220]
with open("input.txt", "r") as f:
    cycle = 0
    x = 1
    for line in f:
        (cycle_inc, modifier) = read_instruction(line.strip())
        logging.debug(f"cycles_curr: {cycle}, inc: {cycle_inc}. x_curr: {x}, modifier {modifier}")
        for i in range(cycle_inc):
            cycle += 1
            if cycle in check_interval:
                logging.debug(f"Reached check interval: ")
                answer += cycle * x
        
        x += modifier

        
        
logging.info(f"answer = {answer}")

