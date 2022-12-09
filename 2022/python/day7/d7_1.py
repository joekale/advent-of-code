import logging
import re

logging.basicConfig(level=logging.DEBUG)

_CD_UP = re.compile(r"^\$\scd\s\.\.")
_CD_DOWN = re.compile(r"^\$\scd\s([a-zA-Z]+)")
_CD_TOP = re.compile(r"^\$\scd\s/")
_LS = re.compile(r"^\$\sls")


answer = 0
directories = {"/": 0}
dirname = "/"
with open("input.txt", "r") as f:
    l = f.readline().strip()
    while l:
        if _LS.match(l):
            logging.debug("list dir")
            l = f.readline().strip()
        elif _CD_TOP.match(l):
            logging.debug("moving to root")
            dirname = "/"
            l = f.readline().strip()
        elif _CD_DOWN.match(l):
            dir = _CD_DOWN.findall(l)[0]
            dirname += dir + "/"
            logging.debug(f"going to dir {dirname}")
            l = f.readline().strip()
        elif _CD_UP.match(l):
            dirname = '/'.join(dirname.split('/')[:-2]) + '/'
            logging.debug(f"moved up to {dirname}")
            l = f.readline().strip()
        else:
            if l.split(' ')[0] == "dir":
                directories[dirname + l.split(' ')[1] + '/'] = 0
                logging.debug(f"see dir {l.split(' ')[1]}")
            else:
                if dirname in directories.keys():
                    directories[dirname] += int(l.split(' ')[0])
                else:
                    raise Exception("Shouldn't have got here")
            
            l = f.readline().strip()

logging.debug(directories)
for key in directories.keys():
    total = 0
    subdirs = [x for x in directories.keys() if x.startswith(key)]
    for dir in subdirs:
        total += directories[dir]

    logging.debug(f"directory {key} total: {total}")

    if total < 100000:
        answer += total

logging.info(f"answer = {answer}")

