lines = []
with open("day5input.txt") as f:
    L = f.readlines()

    for line in L:
        lines.append([l.split(",") for l in line.strip().split("->")])


input_lines = []

max_x, max_y = 0, 0

for line in lines:
    p1 = (int(line[0][0]), int(line[0][1]))
    p2 = (int(line[1][0]), int(line[1][1]))

    max_x = max(max_x, p1[0], p2[0])
    max_y = max(max_y, p1[1], p2[1])

    input_lines.append((p1, p2))

board = [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]

print(len(input_lines))

for line in input_lines:
    [p1, p2] = line

    if p1[0] == p2[0]:
        for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            board[y][p1[0]] += 1

    elif p1[1] == p2[1]:
        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
            board[p1[1]][x] += 1

    else:
        # diagonal on 45 degrees
        x_diff = p2[0] - p1[0]
        y_diff = p2[1] - p1[1]

        # Traverse down the line
        if x_diff > 0:
            x_step = 1
        else:
            x_step = -1

        if y_diff > 0:
            y_step = 1
        else:
            y_step = -1

        x = p1[0]
        y = p1[1]

        while x != p2[0] or y != p2[1]:
            board[y][x] += 1
            x += x_step
            y += y_step
        board[y][x] += 1



# for line in board:
#     for l in line:
#         if l > 0:
#             print(l, end="")
#         else:
#             print(".", end="")
#     print()

count = sum(sum([1 if v > 1 else 0 for v in b]) for b in board)
print("Task 2:", count)

