import numpy as np
from functools import lru_cache


@lru_cache(maxsize=None)
def get_sequence_value(sequence):
    s = "".join([str(int(x)) for x in sequence])
    s = int(s, 2)

    return enhancement_algo[s]


TRUE_TUPLE = (True,) * 9
FALSE_TUPLE = (False,) * 9


def perform_step(puzzle, inf_character):
    puzzle = np.pad(puzzle, pad_width=2, mode="constant", constant_values=inf_character)
    new_puzzle = np.full(puzzle.shape, inf_character, dtype=bool)

    for i in range(1, puzzle.shape[0] - 1):
        for j in range(1, puzzle.shape[1] - 1):
            new_puzzle[i, j] = get_sequence_value(
                puzzle[i - 1 : i + 2, j - 1 : j + 2].tobytes()
            )

    if inf_character:
        inf_character = get_sequence_value(TRUE_TUPLE)
    else:
        inf_character = get_sequence_value(FALSE_TUPLE)

    return new_puzzle[1:-1, 1:-1], inf_character


with open("day20input.txt") as f:
    input = f.read().split("\n\n")

enhancement_algo = input[0].replace("\n", "")
puzzle = input[1].split("\n")

enhancement_algo = [x == "#" for x in enhancement_algo]

puzzle = [[x == "#" for x in line.strip()] for line in puzzle]

puzzle = np.array(puzzle, dtype=bool)

inf_character = 0
num_steps = 50
part_1_steps = 2

for step in range(part_1_steps):
    puzzle, inf_character = perform_step(puzzle, inf_character)

ans1 = np.sum(puzzle)


for step in range(num_steps - part_1_steps):
    puzzle, inf_character = perform_step(puzzle, inf_character)

print("Part 1:", ans1)
print("Part 2:", np.sum(puzzle))
