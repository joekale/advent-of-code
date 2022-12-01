import logging

logging.basicConfig(level=logging.INFO)
most_cals = 0
with open("input.txt", "r") as f:
    elf_load = 0
    for line in f:
        l = line.strip()
        if len(l) > 0:
            logging.debug(l)
            elf_load += int(l)
        else:
            logging.debug("elf load: {elf_load}")
            if elf_load > most_cals:
                most_cals = elf_load
            elf_load = 0

logging.info(f"answer = {most_cals}")

