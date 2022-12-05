import logging

logging.basicConfig(level=logging.INFO)

answer = 0
with open("input.txt", "r") as f:
    for line in f:
        first_pair, second_pair = line.strip().split(',')
        first_hilo = [int(i) for i in first_pair.split('-')]
        second_hilo = [int(j) for j in second_pair.split('-')]
        first_set = set(range(first_hilo[0], first_hilo[1] + 1))
        second_set = set(range(second_hilo[0], second_hilo[1] + 1))
        logging.debug(f"first: {first_set}, second: {second_set}")
        if len(first_set.intersection(second_set)) > 0:
            logging.debug("overlap")
            answer += 1

logging.info(f"answer = {answer}")

