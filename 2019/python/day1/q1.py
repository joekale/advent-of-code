fuel = 0
with open("input.txt", 'r') as f:
    for mass in f.readlines():
        fuel += ((int(mass)//3) - 2)

print("fuel requirement: ", fuel)