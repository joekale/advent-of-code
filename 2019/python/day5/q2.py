def parse_intcode(code):
    code = str(code)
    code = code.zfill(5)
    return int(code[3:5]), int(code[2]), int(code[1]), int(code[0])


def run_opcode(intcodes, position):
    opcode, p1mode, p2mode, p3mode = parse_intcode(intcodes[position])
    if opcode == 99:
        return -1
    elif (opcode == 1):
        first_param = int(intcodes[position+1])
        first_val = int(intcodes[first_param]) if p1mode == 0 else first_param
        second_param = int(intcodes[position+2])
        second_val = int(intcodes[second_param]) if p2mode == 0 else second_param
        print("Adding {} to {} and placing at address {}".format(first_val, second_val, intcodes[position+3]))
        intcodes[int(intcodes[position+3])] = first_val + second_val
        position = position if position == int(intcodes[position +3]) else  position + 4
    elif (opcode == 2):
        first_param = int(intcodes[position+1])
        first_val = int(intcodes[first_param]) if p1mode == 0 else first_param
        second_param = int(intcodes[position+2])
        second_val = int(intcodes[second_param]) if p2mode == 0 else second_param
        print("Multiplying {} to {} and placing at address {}".format(first_val, second_val, intcodes[position+3]))
        intcodes[int(intcodes[position+3])] = first_val * second_val
        position = position if position == int(intcodes[position +3]) else  position + 4
    elif (opcode == 3):
        print("Provide Input")
        in_val = input()
        intcodes[int(intcodes[position+1])] = str(in_val)
        position = position if position == int(intcodes[position +1]) else  position + 2
    elif (opcode == 4):
        print("Test Result = {}".format(int(intcodes[int(intcodes[position+1])])))
        position += 2
    elif (opcode == 5):
        first_param = int(intcodes[position+1])
        first_val = int(intcodes[first_param]) if p1mode == 0 else first_param
        if first_val != 0:
            second_param = int(intcodes[position+2])
            second_val = int(intcodes[second_param]) if p2mode == 0 else second_param
            print("Jumping to position {}".format(second_val))
            position = second_val
        else:
            position += 3
            print("Moving to next instruction: {}".format(position))
    elif (opcode == 6):
        first_param = int(intcodes[position+1])
        first_val = int(intcodes[first_param]) if p1mode == 0 else first_param
        if first_val == 0:
            second_param = int(intcodes[position+2])
            second_val = int(intcodes[second_param]) if p2mode == 0 else second_param
            print("Jumping to position {}".format(second_val))
            position = second_val
        else:
            position += 3
            print("Moving to next instruction: {}".format(position))
    elif (opcode == 7):
        first_param = int(intcodes[position+1])
        first_val = int(intcodes[first_param]) if p1mode == 0 else first_param
        second_param = int(intcodes[position+2])
        second_val = int(intcodes[second_param]) if p2mode == 0 else second_param
        print("Checking {} less than{} and placing at address {}".format(first_val, second_val, intcodes[position+3]))
        intcodes[int(intcodes[position+3])] = first_val < second_val
        position = position if position == int(intcodes[position +3]) else  position + 4
    elif (opcode == 8):
        first_param = int(intcodes[position+1])
        first_val = int(intcodes[first_param]) if p1mode == 0 else first_param
        second_param = int(intcodes[position+2])
        second_val = int(intcodes[second_param]) if p2mode == 0 else second_param
        print("Checking {} less than{} and placing at address {}".format(first_val, second_val, intcodes[position+3]))
        intcodes[int(intcodes[position+3])] = first_val == second_val
        position = position if position == int(intcodes[position +3]) else  position + 4
    
    return position


text = ""
with open("day5/input.txt", 'r') as f:
    text = f.read()

intcodes = text.split(',')

position = 0
while(True):
    position = run_opcode(intcodes, position)
    if position == -1:
        break

print("TEST Complete. Diagnostic Code is final test output")