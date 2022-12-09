import logging
import math 

logging.basicConfig(level=logging.DEBUG)

def calc_distance(H, T):
    logging.debug(f"H: ({H[0]}, {H[1]}), T: ({T[0]}, {T[1]})")
    return int(math.sqrt((H[0] - T[0])**2 + (H[1] - T[1])**2))

answer = 0
visited = set()
H = (0,0)
T = (0,0)
with open("input.txt", "r") as f:
    visited.add(T)
    for line in f:
        l = line.strip()
        if l:
            (dir, distance) = l.split()
            if dir == 'U':
                for _ in range(1, int(distance) + 1):
                    H_last = H
                    H = (H[0], H[1] + 1)
                    if (calc_distance(H, T) > 1):
                        T = H_last
                        visited.add(T)
            elif dir == 'D':
                for _ in range(1, int(distance) + 1):
                    H_last = H
                    H = (H[0], H[1] - 1)
                    if (calc_distance(H, T) > 1):
                        T = H_last
                        visited.add(T)

            elif dir == 'L':
                for _ in range(1, int(distance) + 1):
                    H_last = H
                    H = (H[0] - 1, H[1])
                    if (calc_distance(H, T) > 1):
                        T = H_last
                        visited.add(T)

            elif dir == 'R':
                for _ in range(1, int(distance) + 1):
                    H_last = H
                    H = (H[0] + 1, H[1])
                    if (calc_distance(H, T) > 1):
                        T = H_last
                        visited.add(T)
            
            else:
                raise Exception("Shouldn't get here")
        

answer = len(visited)
logging.info(f"answer = {answer}")

