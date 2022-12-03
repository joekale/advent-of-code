import logging

logging.basicConfig(level=logging.INFO)

answer = 0
with open("input.txt", "r") as f:
    group = []
    for line in f:
        group.append(line.strip())
        if len(group) == 3:
            shared_value = [x for x in group[0] for y in group[1] for z in group[2] if x == y and y == z][0]
            answer += ord(shared_value) - 0x60 if shared_value.islower() else ord(shared_value) - 0x40 + 26
            logging.debug(f"shared: {shared_value}")
            group.clear()

logging.info(f"answer = {answer}")

