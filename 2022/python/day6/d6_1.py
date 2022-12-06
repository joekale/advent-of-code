import logging
import re

logging.basicConfig(level=logging.INFO)

answer = 0
with open("input.txt", "r") as f:
    line = f.read().strip()

for i in range(3, len(line)):
    chars = set(line[i-3:i+1])
    logging.debug(f"i: {i}, chars: {chars}, {len(chars)}")
    if len(chars) == 4:
        logging.info("Packet Found")
        answer = i + 1
        break

logging.info(f"answer = {answer}")

