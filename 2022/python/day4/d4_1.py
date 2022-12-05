import logging

logging.basicConfig(level=logging.INFO)

answer = 0
with open("input.txt", "r") as f:
    for line in f:
        first_pair, second_pair = line.strip().split(',')
        first_set = first_pair.split('-')
        second_set = second_pair.split('-')
        logging.debug(f"first: {first_set}, second: {second_set}")
        if (int(first_set[0]) >= int(second_set[0]) and int(first_set[1]) <= int(second_set[1])) or \
            (int(second_set[0]) >= int(first_set[0]) and int(second_set[1]) <= int(first_set[1])):
            logging.debug("subset")
            answer += 1

logging.info(f"answer = {answer}")

