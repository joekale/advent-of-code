
with open("python/day1/d1.txt") as f:
    content = f.readlines()

count = 0
iterator = iter(content)
current = next(iterator)
while(True):
    try:
        nxt = next(iterator)
        print(f"current: {current}, next: {nxt}")
        if int(current) < int(nxt):
            count += 1
        current = nxt
    except StopIteration:
        break

print(count)