with open("python/day1/d1.txt") as f:
    content = [int(i) for i in f]

print(sum([sum(content[i:i+3]) < sum(content[i+1:i+4]) for i in range(0, len(content) - 2)]))