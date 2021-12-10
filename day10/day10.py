CLOSING_TABLE = {")": "(", "}": "{", "]": "[", ">": "<"}

FLIPPED_CLOSING_TABLE = {v: k for k, v in CLOSING_TABLE.items()}

SCORING_TABLE_1 = {")": 3, "]": 57, "}": 1197, ">": 25137}

SCORING_TABLE_2 = {")": 1, "]": 2, "}": 3, ">": 4}


def find_illegal_char(line):
    stack = []
    for c in line:
        if c in CLOSING_TABLE.keys():
            if not stack or stack.pop() != CLOSING_TABLE[c]:
                return c
        else:
            stack.append(c)
    return None


def get_remaining_part(line):
    stack = []

    for c in line:
        if c in CLOSING_TABLE.keys():
            if not stack or stack.pop() != CLOSING_TABLE[c]:
                return None
        else:
            stack.append(c)

    if stack:
        stack.reverse()
        stack = [FLIPPED_CLOSING_TABLE[c] for c in stack]

        return "".join(stack)

    else:
        return None


with open("day10input.txt") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

s = 0
for line in lines:
    if illegal_char := find_illegal_char(line):
        s += SCORING_TABLE_1[illegal_char]

print("Part 1 Score:", s)

scores = []
for line in lines:
    small_score = 0
    if remaining := get_remaining_part(line):
        for c in remaining:
            small_score *= 5

            small_score += SCORING_TABLE_2[c]

        scores.append(small_score)

scores.sort()
# print middle score
print("Part 2 Score:", scores[len(scores) // 2])
