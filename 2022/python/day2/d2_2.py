import logging

logging.basicConfig(level=logging.INFO)

lookup = {"A": {"val": 1, "win": "C", "lose": "B"},
          "B": {"val": 2, "win": "A", "lose": "C"},
          "C": {"val": 3, "win": "B", "lose": "A"}}

total = 0
with open("input.txt", "r") as f:
    for line in f:
        l = line.strip()
        if l:
            opp, me = l.split()
            logging.debug(f"opp: {opp}, me: {me}")
            if me == "Y":
                logging.debug(f"draw {lookup[opp]['val']} + 3")
                total += lookup[opp]["val"] + 3
            elif me == "Z":
                logging.debug(f"win {lookup[lookup[opp]['lose']]['val']} + 6")
                total += lookup[lookup[opp]["lose"]]["val"] + 6
            else:
                logging.debug(f"loss {lookup[lookup[opp]['win']]['val']} + 0")
                total += lookup[lookup[opp]["win"]]["val"]


logging.info(f"answer = {total}")

