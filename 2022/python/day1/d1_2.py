import logging

logging.basicConfig(level=logging.INFO)

elf_loads = []
with open("input.txt", "r") as f:
    most_cals = 0
    elf_load = 0
    for line in f:
        l = line.strip()
        if len(l) > 0:
            logging.debug(l)
            elf_load += int(l)
        else:
            logging.debug(f"elf load: {elf_load}")
            elf_loads.append(elf_load)
            elf_load = 0

answer = sum(sorted(elf_loads)[-3:])
logging.info(f"answer = {answer}")

