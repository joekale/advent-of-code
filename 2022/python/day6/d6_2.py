import logging
import re

logging.basicConfig(level=logging.INFO)

answer = 0
with open("input.txt", "r") as f:
    line = f.read().strip()

packet = 0
for i in range(3, len(line)):
    chars = set(line[i-3:i+1])
    logging.debug(f"i: {i}, chars: {chars}, {len(chars)}")
    if len(chars) == 4:
        logging.info(f"Packet Found")
        packet = i
        break

for i in range(i+14, len(line)):
    chars = set(line[i-13:i+1])
    logging.debug(f"i: {i}, chars: {chars}, {len(chars)}")
    if len(chars) == 14:
        logging.info(f"Message Found")
        answer = i + 1
        break

logging.info(f"answer = {answer}")

