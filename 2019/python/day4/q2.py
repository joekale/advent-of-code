def has_repeat(val):
    text = str(val)
    contains_repeat = False
    i = 0
    while i < len(text) - 1:
        repeat = 1
        while text[i] == text[i+1]:
            repeat += 1
            i += 1
            if i > len(text) - 2:
                break
        
        i += 1
        contains_repeat = contains_repeat or repeat == 2
    
    return contains_repeat


def does_increase(val):
    text = str(val)
    increases = True
    for i in range(0, len(text) - 1):
        increases = increases and int(text[i+1]) >= int(text[i])
    
    return increases


input = "234208-765869"

pwrange = input.split("-",maxsplit=1)

pw_possible = 0
for i in range(int(pwrange[0]), int(pwrange[1]) + 1):
    valid = True
    valid = valid and has_repeat(i)
    valid = valid and does_increase(i)
    if valid:
        pw_possible += 1

print(pw_possible)