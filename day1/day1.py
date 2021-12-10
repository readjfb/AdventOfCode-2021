with open("day1input.txt") as f:
    lines = f.readlines()

all_lines = []

# Part 1
for line in lines:
    line = line.strip()
    line = int(line)

    all_lines.append(line)

increasing, decreasing = 0, 0

for i, line in enumerate(all_lines[1:]):
    if line > all_lines[i]:
        increasing += 1
    if line < all_lines[i]:
        decreasing += 1

print("Part 1:", increasing)

# Part 2
# Count the number of times that the sum of a 3 number window increases and decreases

increasing_2, decreasing_2 = 0, 0
previous_sum = -1000

for i, line in enumerate(all_lines[2:], 2):
    s = line + all_lines[i - 1] + all_lines[i - 2]

    if s > previous_sum:
        increasing_2 += 1
    if s < previous_sum:
        decreasing_2 += 1

    previous_sum = s

increasing_2 -= 1
print(f"Part 2: {increasing_2}")
