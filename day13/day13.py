with open("day13input.txt") as f:
    lines = f.read().strip()

coordinates, folds = lines.split("\n\n")

coordinates = coordinates.split("\n")
folds = folds.split("\n")

max_x = max(map(lambda x: int(x.split(",")[0]), coordinates))
max_y = max(map(lambda x: int(x.split(",")[1]), coordinates))

paper = [[False for _ in range(max_x + 1)] for _ in range(max_y + 1)]

for coordinate in coordinates:
    x, y = map(int, coordinate.split(","))
    paper[y][x] = True


def perform_fold(paper, fold):
    instruction = fold.split(" ")[2]

    axis, value = instruction.split("=")
    value = int(value)

    if axis == "y":
        new_paper = [[False] * len(paper[0]) for _ in range(value)]

        for ny in range(0, len(paper) - 1 - value):
            for x in range(len(paper[0])):
                new_paper[ny][x] = paper[-(ny + 1)][x] or paper[ny][x]
        return new_paper

    elif axis == "x":
        new_paper = [[False] * value for _ in range(len(paper))]

        for y in range(len(paper)):
            for nx in range(0, len(paper[y]) - 1 - value):
                new_paper[y][nx] = paper[y][-(nx + 1)] or paper[y][nx]
        return new_paper


# Part 1
paper = perform_fold(paper, folds[0])

p1_sum = sum(sum(row) for row in paper)
print(f"Part 1: {p1_sum}")

for line in folds[1:]:
    paper = perform_fold(paper, line)

for line in paper:
    print("".join(["#" if x else " " for x in line]))
