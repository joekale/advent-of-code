import logging
import re

_RE_ROW_SPLIT = re.compile(r"(?:(?:([(A-Z)]|\s\s\s\s)))")
_RE_MOVES = re.compile(r"(?:move\s(\d+))\s(?:from\s(\d+))\s(?:to\s(\d+))")

logging.basicConfig(level=logging.DEBUG)

answer = ""
stacks = []
with open("input.txt", "r") as f:
    parsing = True
    for line in f:
        if parsing:
            l = _RE_ROW_SPLIT.findall(line.rstrip())
            if len(l) == 0:
                parsing = False
                logging.warning(f"stack post parsing: {stacks}")

            for i, val in enumerate(l):
                if len(stacks) <= i:
                    stacks.append(list())

                if val.strip() != '': 
                    stacks[i].insert(0, val)

        else:
            l = _RE_MOVES.findall(line.strip())
            logging.debug(f"{l}")
            if len(l) == 0:
                continue
            else:
                l = [int(g) for g in list(l[0])];
                logging.debug(f"{l}")
                for i in range(l[0]):
                    stacks[l[2] - 1].append(stacks[l[1] - 1].pop())
                    logging.debug(f"moved: {stacks}")

for stack in stacks:
    answer += stack.pop() 

logging.info(f"answer = {answer}")

