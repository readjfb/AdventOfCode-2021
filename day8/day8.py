# Pretty basic way of doing this, just used logic to find each letter, then
# refrenced the table to find the corresponding number
# There's definitely cooler ways of doing this, but this is O(1)
KNOWN_TABLE = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def get_n_times(string, n):
    return set(filter(lambda x: string.count(x) == n, string))


def decode(sig_patterns, message):
    sig_patterns = [set(x for x in p) for p in sig_patterns]
    message = message

    one = [x for x in sig_patterns if len(x) == 2][0]
    four = [x for x in sig_patterns if len(x) == 4][0]
    eight = [x for x in sig_patterns if len(x) == 7][0]
    seven = [x for x in sig_patterns if len(x) == 3][0]

    fives = [x for x in sig_patterns if len(x) == 5]
    sixes = [x for x in sig_patterns if len(x) == 6]

    knowns = {}

    # create single list with sum of all fives, sixes
    fives_joined = "".join([str("".join(list(x))) for x in fives])
    sixes_joined = "".join([str("".join(list(x))) for x in sixes])
    joined = fives_joined + sixes_joined

    # Isolate a
    a_possibilities = seven - one
    knowns["a"] = a_possibilities.pop()

    # Element that appears 3x is e
    e_possibilities = get_n_times(joined, 3)
    knowns["e"] = e_possibilities.pop()

    # Element that is in 8 but not in 1, 7, 4 and is not e is g
    g_possibilities = eight - one - seven - four - set(knowns.values())
    knowns["g"] = g_possibilities.pop()

    # Element that appears once in the fives_joined and is not e is b
    b_possibilities = get_n_times(fives_joined, 1) - set(knowns.values())
    knowns["b"] = b_possibilities.pop()

    # D is 4 - 1 - knowns
    d_possibilities = four - one - set(knowns.values())
    knowns["d"] = d_possibilities.pop()

    # C appears twice in the sixes_joined and is not e
    c_possibilities = get_n_times(sixes_joined, 2) - set(knowns.values())
    knowns["c"] = c_possibilities.pop()

    # F appears in 8 and has not been selected yet
    f_possibilities = eight - set(knowns.values())
    knowns["f"] = f_possibilities.pop()

    digits = []

    reversed_knowns = {v: k for k, v in knowns.items()}

    for message_pattern in message:
        letters = "".join(sorted([reversed_knowns[x] for x in message_pattern]))

        if letters in KNOWN_TABLE:
            digits.append(KNOWN_TABLE[letters])

    return digits


fully_split = []

with open("day8input.txt") as f:
    lines = f.readlines()

for line in lines:
    l = line.strip().split("|")

    fully_split.append((l[0].strip().split(" "), l[1].strip().split(" ")))


running_count = []
output_digits = []
for line in fully_split:
    decoded = decode(*line)

    running_count += decoded

    output_digits.append(int("".join(str(x) for x in decoded)))


part1answer = sum(running_count.count(x) for x in (1, 4, 7, 8))
part2answer = sum(output_digits)

print("Part 1: {}".format(part1answer))
print("Part 2: {}".format(part2answer))
