
lines = []
with open("day7input.txt") as f:
    lines = f.readlines()[0].split(",")

lines = [int(x) for x in lines]

min_diff = max(lines) ** len(lines)
min_point = 0

for endpoint in range(min(lines), max(lines)+1):
    diff = 0
    for point in lines:
        n = abs(point - endpoint)
        diff += (n * (n + 1)) // 2

    if diff < min_diff:
        min_diff = diff
        min_point = endpoint

print(min_point, min_diff)


