lines = []
with open("day7input.txt") as f:
    lines = f.readlines()[0].split(",")

lines = [int(x) for x in lines]

# This is crazy inneficient, but it works
min_diff1 = max(lines) ** len(lines)
min_diff2 = max(lines) ** len(lines)

for endpoint in range(min(lines), max(lines)):
    diff1, diff2 = 0, 0
    for point in lines:
        n = abs(point - endpoint)

        diff1 += n
        diff2 += (n * (n + 1)) // 2

    min_diff1 = min(min_diff1, diff1)
    min_diff2 = min(min_diff2, diff2)

print("Part 1:", min_diff1)
print("Part 2", min_diff2)