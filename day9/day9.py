with open("day9input.txt") as f:
    lines = f.readlines()

heightmap = [[9] * (2 + len(lines[0].strip()))]

for line in lines:
    heightmap.append([9] + [int(x) for x in line.strip()] + [9])

heightmap.append([9] * len(heightmap[0]))

# Part 1
# find lowpoints
lowpoints = []
for i in range(1, len(heightmap) - 1):
    for j in range(1, len(heightmap[i]) - 1):
        if heightmap[i][j] < min(
            heightmap[i - 1][j],
            heightmap[i + 1][j],
            heightmap[i][j - 1],
            heightmap[i][j + 1],
        ):
            lowpoints.append((i, j))

risklevels = [1 + heightmap[pt[0]][pt[1]] for pt in lowpoints]

print("Part 1:", sum(risklevels))

# part 2
# find basins with exterior edge 9
basin_sizes = []
points_to_visit = []

for point in lowpoints:
    points_to_visit.append(point)
    size = 0

    while len(points_to_visit) > 0:
        pt = points_to_visit.pop()
        if heightmap[pt[0]][pt[1]] == 9:
            continue
        size += 1

        heightmap[pt[0]][pt[1]] = 9

        points_to_visit.append((pt[0] - 1, pt[1]))
        points_to_visit.append((pt[0] + 1, pt[1]))
        points_to_visit.append((pt[0], pt[1] - 1))
        points_to_visit.append((pt[0], pt[1] + 1))

    basin_sizes.append(size)

basin_sizes.sort(reverse=True)

a = 1
for i in basin_sizes[:3]:
    a *= i

print("Part 2:", a)
