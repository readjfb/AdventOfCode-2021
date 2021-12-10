with open("day2input.txt") as f:
    lines = f.readlines()


inp_lines = []
for line in lines:
    inp_lines.append((line.strip().split(" ")))

horizontal_pos, vertical_pos = 0, 0

for line in inp_lines:
    if line[0] == "forward":
        horizontal_pos += int(line[1])
    elif line[0] == "down":
        vertical_pos += int(line[1])
    elif line[0] == "up":
        vertical_pos -= int(line[1])

print(horizontal_pos, vertical_pos, horizontal_pos * vertical_pos)

# Part 2
horizontal_pos_2, vertical_pos_2, aim = 0, 0, 0

for line in inp_lines:
    if line[0] == "forward":
        horizontal_pos_2 += int(line[1])
        vertical_pos_2 += int(line[1]) * aim

    elif line[0] == "down":
        aim += int(line[1])

    elif line[0] == "up":
        aim -= int(line[1])

print(horizontal_pos_2, vertical_pos_2, horizontal_pos_2 * vertical_pos_2)
