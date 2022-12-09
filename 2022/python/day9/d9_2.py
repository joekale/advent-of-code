import logging
import math 
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)
logging.getLogger('PIL').setLevel(logging.INFO)



def calc_distance(H, T):
    return int(math.sqrt((H[0] - T[0])**2 + (H[1] - T[1])**2))

def update_rope(H_last, knots):
    t = knots[0]
    for i in range(1, len(knots)):
        logging.debug(f"iterating: {knots}")

        # fig, ax = plt.subplots(figsize=(10, 6))
        # ax.axes.grid(visible=True)
        # ax.set_xlim(-10, 15)
        # ax.set_ylim(-10, 15)
        # r1, r2 = map(list, zip(*knots))
        # ax.scatter(x=r1, y=r2)
        # plt.show()

        if calc_distance(t, knots[i]) > 1:
            temp = knots[i]
            temp = (temp[0] + ((t[0] > temp[0]) - (t[0] < temp[0])), temp[1] + ((t[1] > temp[1]) - (t[1] < temp[1])))
            knots[i] = temp
            t = knots[i]
        else:
            break

    return knots

answer = 0
visited = set()
knots = [(0,0) for i in range(10)]
with open("input.txt", "r") as f:
    visited.add(knots[-1])
    for line in f:
        l = line.strip()
        if l:
            (dir, distance) = l.split()
            if dir == 'U':
                for _ in range(1, int(distance) + 1):
                    H_last = knots[0]
                    H = (knots[0][0], knots[0][1] + 1)
                    knots[0] = H
                    knots = update_rope(H_last, knots)
                    visited.add(knots[-1])
            elif dir == 'D':
                for _ in range(1, int(distance) + 1):
                    H_last = knots[0]
                    H = (knots[0][0], knots[0][1] - 1)
                    knots[0] = H
                    knots = update_rope(H_last, knots)
                    visited.add(knots[-1])

            elif dir == 'L':
                for _ in range(1, int(distance) + 1):
                    H_last = knots[0]
                    H = (knots[0][0] - 1, knots[0][1])
                    knots[0] = H
                    knots = update_rope(H_last, knots)
                    visited.add(knots[-1])

            elif dir == 'R':
                for _ in range(1, int(distance) + 1):
                    H_last = knots[0]
                    H = (knots[0][0] + 1, knots[0][1])
                    knots[0] = H
                    knots = update_rope(H_last, knots)
                    visited.add(knots[-1])
            
            else:
                raise Exception("Shouldn't get here")
            
            logging.debug(knots)

answer = len(visited)
logging.info(f"answer = {answer}")

