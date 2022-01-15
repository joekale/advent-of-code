from typing import Dict

def parse_file(file):
    for line in file:
        portions = line.split('|')
        yield portions[0].strip().split(), portions[1].strip().split()

def analyze_sequence(sequence: list) -> Dict[str, int]:
    mapping = {}
    by_length = {7: 8, 3: 7, 4: 4, 2: 1}
    unmapped = list()
    for value in sequence:
        try:
            mapping[frozenset(value)] = by_length[len(value)]
        except KeyError:
            unmapped.append(value)
            continue

    for value in unmapped:
        if len(value) == 6: # 0, 6, 9
            if set([key for key in mapping.keys() if len(key) == 2][0]).union(set(value)) != set(value):
                mapping[frozenset(value)] = 6
            elif len(set([key for key in mapping.keys() if len(key) == 4][0]).intersection(set(value))) == 4:
                mapping[frozenset(value)] = 9
            else:
                mapping[frozenset(value)] = 0
        elif len(value) == 5: # 2, 3, 5
            if set([key for key in mapping.keys() if len(key) == 2][0]).union(set(value)) == set(value):
                mapping[frozenset(value)] = 3
            elif len(set([key for key in mapping.keys() if len(key) == 4][0]).intersection(set(value))) == 2:
                mapping[frozenset(value)] = 2
            else:
                mapping[frozenset(value)] = 5

    return mapping

total = 0
with open("python/day8/d8.txt") as f:
    for sequence, output in parse_file(f):
        mapping = analyze_sequence(sequence)
        val = ""
        for value in output:
            val += str(mapping[frozenset(value)])
        
        total += int(val)

print(total)     