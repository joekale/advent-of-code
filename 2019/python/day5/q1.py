def parse_intcode(code):
    code = str(code)
    code = code.zfill(5)
    return int(code[3:5]), int(code[2]), int(code[1]), int(code[0])


def run_opcode(intcodes, position):
    opcode, p1mode, p2mode, p3mode = parse_intcode(intcodes[position])
    jump = 4
    if opcode == 99:
        return 0
    elif (opcode == 1):
        first_param = int(intcodes[position+1])
        first_val = int(intcodes[first_param]) if p1mode == 0 else first_param
        second_param = int(intcodes[position+2])
        second_val = int(intcodes[second_param]) if p2mode == 0 else second_param
        print("Adding {} to {} and placing at address {}".format(first_val, second_val, intcodes[position+3]))
        intcodes[int(intcodes[position+3])] = first_val + second_val
    elif (opcode == 2):
        first_param = int(intcodes[position+1])
        first_val = int(intcodes[first_param]) if p1mode == 0 else first_param
        second_param = int(intcodes[position+2])
        second_val = int(intcodes[second_param]) if p2mode == 0 else second_param
        print("Multiplying {} to {} and placing at address {}".format(first_val, second_val, intcodes[position+3]))
        intcodes[int(intcodes[position+3])] = first_val * second_val
    elif (opcode == 3):
        print("Provide Input")
        in_val = input()
        intcodes[int(position+1)] = str(in_val)
        jump = 2
    elif (opcode == 4):
        print("Test Result = {}".format(int(intcodes[int(intcodes[position+1])])))
        jump = 2
    
    return jump

text = ""
with open("2019/inputs/5.txt", 'r') as f:
    text = f.read()

intcodes = text.split(',')

position = 0
while(True):
    jump = run_opcode(intcodes, position)
    if jump == 0:
        break
    position += jump

print("TEST Complete. Diagnostic Code is final test output")