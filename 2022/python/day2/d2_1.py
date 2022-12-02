import logging

logging.basicConfig(level=logging.INFO)

lookup = {"X": {"val": 1, "win": "C", "eq": "A"},
          "Y": {"val": 2, "win": "A", "eq": "B"},
          "Z": {"val": 3, "win": "B", "eq": "C"}}

total = 0
with open("input.txt", "r") as f:
    for line in f:
        l = line.strip()
        if l:
            opp, me = l.split()
            logging.debug(f"opp: {opp}, me: {me}")
            if opp == lookup[me]["eq"]:
                logging.debug(f"draw {lookup[me]['val']} + 3")
                total += lookup[me]["val"] + 3
            elif opp == lookup[me]["win"]:
                logging.debug(f"win {lookup[me]['val']} + 6")
                total += lookup[me]["val"] + 6
            else:
                logging.debug(f"loss {lookup[me]['val']} + 0")
                total += lookup[me]["val"]


logging.info(f"answer = {total}")

