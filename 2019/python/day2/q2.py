from copy import deepcopy

def test_inputs(memory, noun, verb):
    intcodes = deepcopy(memory)
    intcodes[1] = noun
    intcodes[2] = verb

    halt = False
    position = 0
    while(halt != True):
        opcode = int(intcodes[position])
        if opcode == 99:
            halt = True
        elif (opcode == 1):
            intcodes[int(intcodes[position+3])] = int(intcodes[int(intcodes[position+1])]) + int(intcodes[int(intcodes[position+2])])
        elif (opcode == 2):
            intcodes[int(intcodes[position+3])] = int(intcodes[int(intcodes[position+1])]) * int(intcodes[int(intcodes[position+2])])
        
        position += 4

    return intcodes[0]


text = ""
with open("input.txt", 'r') as f:
    text = f.read()

intcodes = text.split(',')

noun = 0
verb = 0
for i in range(0, 100):
    for j in range(0, 100):
        if test_inputs(intcodes,i,j) == 19690720:
            noun = i
            verb = j
            break


print("100 * {} + {} = {}".format(noun, verb, 100 * noun + verb))