def parse_file(file):
    for line in file:
        portions = line.split('|')
        yield portions[0].strip().split(), portions[1].strip().split()

counts = [0] * 10
by_length = {7: 8, 3: 7, 4: 4, 2: 1}
with open("python/day8/d8.txt") as f:
    for first, second in parse_file(f):
        tracking = {}
        # for segment in first:
        #     if len(segment) == 2:
        #         tracking[segment] = 1
        #     elif len(segment) == 4:
        #         tracking[segment] = 4
        #     elif len(segment) == 3:
        #         tracking[segment] = 7
        #     elif len(segment) == 7:
        #         tracking[segment] = 8

        for  output in second:
            try:
                counts[by_length[len(output)]] += 1
            except KeyError:
                continue

print(sum(counts))     