# Part 1 is done the naive way, with the actual string
# Part 2 is done with a table of frequencies and caching

with open("day14input.txt") as f:
    data = f.read().strip()

sequence, rules = data.split("\n\n")
sequence_copy = sequence

rules = [rule.split(" -> ") for rule in rules.split("\n")]
rules = {pair: c for pair, c in rules}


def naive_solution(sequence, time):
    for step in range(time):
        new_sequence = sequence

        i = 0
        while i < len(new_sequence) - 1:
            c = rules.get(new_sequence[i : i + 2], None)
            if c:
                new_sequence = new_sequence[: i + 1] + c + new_sequence[i + 1 :]
                i += 1
            i += 1

        sequence = new_sequence
    return sequence


sequence = naive_solution(sequence, 10)

counts = {}
for i in sequence:
    counts[i] = counts.get(i, 0) + 1

part1_solution = max(counts.values()) - min(counts.values())
print(f"Part 1: {part1_solution}")

# Part 2
sequence = sequence_copy
rule_table = {key: [key[0] + value, value + key[1]] for key, value in rules.items()}


def find_solution(sequence, times):
    pairs = [sequence[i : i + 2] for i in range(len(sequence) - 1)]

    frequencies = {key: pairs.count(key) for key in pairs}

    for step in range(times):
        new_frequencies = {}

        for pair, time in frequencies.items():
            for item in rule_table[pair]:
                new_frequencies[item] = new_frequencies.get(item, 0) + time

        frequencies = new_frequencies

    letter_counts = {sequence[0]: 1}
    letter_counts[sequence[-1]] = letter_counts.get(sequence[-1], 0) + 1

    for pair, time in frequencies.items():
        letter_counts[pair[0]] = letter_counts.get(pair[0], 0) + time
        letter_counts[pair[1]] = letter_counts.get(pair[1], 0) + time

    return (max(letter_counts.values()) - min(letter_counts.values())) // 2


print("Part 2:", find_solution(sequence_copy, 40))
