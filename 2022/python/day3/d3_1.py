import logging

logging.basicConfig(level=logging.INFO)

answer = 0
with open("input.txt", "r") as f:
    for line in f:
        l = line.strip()
        first = l[:len(l)//2]
        second = l[len(l)//2:]
        shared_value = [x for x in first for y in second if x == y][0]
        answer += ord(shared_value) - 0x60 if shared_value.islower() else ord(shared_value) - 0x40 + 26
        logging.debug(f"first: {first}, second: {second}, shared: {shared_value}")

logging.info(f"answer = {answer}")

