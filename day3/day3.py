def bin2int(s):
    return sum(int(c) * (2 ** i) for i, c in enumerate(s[::-1]))


def find_most_common_bit(bits, most_common=True):
    bit_sums = [0 for i in range(len(bits[0]))]

    for line in bits:
        for i, c in enumerate(line):
            bit_sums[i] += int(c)

    bit_sums = [bs / len(bits) for bs in bit_sums]

    if most_common:
        return [int(b >= 0.5) for b in bit_sums]
    else:
        return [int(b < 0.5) for b in bit_sums]


lines = []
with open("day3input.txt") as f:
    L = f.readlines()

    for line in L:
        lines.append((line.strip()))

# Part 1
most_common = find_most_common_bit(lines)
gamma = bin2int(most_common)
least_common = [not b for b in most_common]
epsilon = bin2int(least_common)

consumption = gamma * epsilon

print("Part 1:", consumption)

# Part 2
# Find oxygen generator rating first
possible_values = [x for x in lines]

for i in range(len(lines[0])):
    new_values = []

    most_common = find_most_common_bit(possible_values, most_common=True)

    for line in possible_values:
        if str(most_common[i]) == line[i]:
            new_values.append(line)

    possible_values = list(new_values)

    if len(possible_values) == 1:
        break

ox_rating = bin2int(possible_values[0])

# Find CO2 generator rating
possible_values = [x for x in lines]

for i in range(len(lines[0])):
    new_values = []

    least_common = find_most_common_bit(possible_values, most_common=False)

    for line in possible_values:
        if str(least_common[i]) == line[i]:
            new_values.append(line)

    possible_values = list(new_values)

    if len(possible_values) == 1:
        break

o2_rating = bin2int(possible_values[0])

print("Part 2:", ox_rating * o2_rating)
