
def calc_required_fuel(fuel):
    to_add = (fuel//3) - 2
    if to_add <= 0:
        return 0;
    
    return to_add + calc_required_fuel(to_add)


fuel = 0
with open("input.txt", 'r') as f:
    for mass in f.readlines():
        fuel += calc_required_fuel(int(mass))

print("Total fuel requirement: ", fuel)