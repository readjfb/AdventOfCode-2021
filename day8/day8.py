KNOWN_TABLE = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}
# flip keys and values of known table
KNOWN_TABLE = {v: k for k, v in KNOWN_TABLE.items()}


class Decoder:
    def __init__(self, sig_patterns, message):
        self.sig_patterns = [set(x for x in p) for p in sig_patterns]
        self.message = message

        self.one = next(filter(lambda x: len(x) == 2, self.sig_patterns))
        self.four = next(filter(lambda x: len(x) == 4, self.sig_patterns))
        self.eight = next(filter(lambda x: len(x) == 7, self.sig_patterns))
        self.seven = next(filter(lambda x: len(x) == 3, self.sig_patterns))

        self.fives = list(filter(lambda x: len(x) == 5, self.sig_patterns))
        self.sixes = list(filter(lambda x: len(x) == 6, self.sig_patterns))

        self.knowns = {}

    def find_knowns(self):
        # create single list with sum of all fives, sixes
        fives_joined = "".join([str("".join(list(x))) for x in self.fives])
        sixes_joined = "".join([str("".join(list(x))) for x in self.sixes])
        joined = fives_joined + sixes_joined

        # Isolate a
        a_possibilities = self.seven - self.one
        self.knowns["a"] = a_possibilities.pop()

        # Element that appears 3x is e
        e_possibilities = set(filter(lambda x: joined.count(x) == 3, joined))
        self.knowns["e"] = e_possibilities.pop()

        # Element that is in 8 but not in 1, 7, 4 and is not e is g
        g_possibilities = (
            self.eight - self.one - self.seven - self.four - set(self.knowns.values())
        )
        self.knowns["g"] = g_possibilities.pop()

        # Element that appears once in the fives_joined and is not e is b
        b_possibilities = set(
            filter(lambda x: fives_joined.count(x) == 1, fives_joined)
        ) - set(self.knowns.values())
        self.knowns["b"] = b_possibilities.pop()

        # D is 4 - 1 - knowns
        d_possibilities = self.four - self.one - set(self.knowns.values())
        self.knowns["d"] = d_possibilities.pop()

        # C appears twice in the sixes_joined and is not e
        c_possibilities = set(
            filter(lambda x: sixes_joined.count(x) == 2, sixes_joined)
        ) - set(self.knowns.values())
        self.knowns["c"] = c_possibilities.pop()

        # F appears in 8 and has not been selected yet
        f_possibilities = self.eight - set(self.knowns.values())
        self.knowns["f"] = f_possibilities.pop()

    def decode_message(self):
        digits = []

        flipped_knowns = {v: k for k, v in self.knowns.items()}

        for message_pattern in self.message:
            message_letters = "".join(
                sorted([flipped_knowns[x] for x in message_pattern])
            )

            if message_letters in KNOWN_TABLE:
                digits.append(KNOWN_TABLE[message_letters])

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
    d = Decoder(*line)
    d.find_knowns()

    decoded = d.decode_message()

    running_count += decoded

    output_digits.append(sum([x * (10 ** i) for i, x in enumerate(decoded[::-1])]))


part1answer = sum(running_count.count(x) for x in (1, 4, 7, 8))
part2answer = sum(output_digits)

print("Part 1: {}".format(part1answer))
print("Part 2: {}".format(part2answer))
