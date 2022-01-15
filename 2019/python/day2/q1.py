text = ""
with open("input.txt", 'r') as f:
    text = f.read()

intcodes = text.split(',')

intcodes[1] = 12
intcodes[2] = 2

halt = False
position = 0
while(halt != True):
    opcode = int(intcodes[position])
    if opcode == 99:
        halt = True
    elif (opcode == 1):
        print("found opcode 1 adding")
        intcodes[int(intcodes[position+3])] = int(intcodes[int(intcodes[position+1])]) + int(intcodes[int(intcodes[position+2])])
    elif (opcode == 2):
        print("found opcode 2 multiplying")
        intcodes[int(intcodes[position+3])] = int(intcodes[int(intcodes[position+1])]) * int(intcodes[int(intcodes[position+2])])
    
    position += 4

print(intcodes[0])