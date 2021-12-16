import heapq
import numpy as np

with open("day15input.txt") as f:
    data = f.read().strip()

risks = [[int(x) for x in line] for line in data.split("\n")]

def find_shortest_path(risks) -> int:
    len_x, len_y = risks.shape

    finalized = set()
    heap = [(0, (len_x - 1, len_y - 1))]

    while heap:
        value, item = heapq.heappop(heap)

        if item == (0, 0):
            return value - risks[0, 0] + risks[-1, -1]

        if item in finalized:
            continue

        finalized.add(item)

        x, y = item

        for neigh in ((x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)):
            if (
                len_y > neigh[1] >= 0
                and len_x > neigh[0] >= 0
                and neigh not in finalized
            ):
                heapq.heappush(heap, (risks[neigh[1], neigh[0]] + value, neigh))

    print("ERROR NO PATH FOUND!")
    return None

risks = np.array(risks)
print("Part 1:", find_shortest_path(risks))

fd = []
for r in range(5):
    a = [((risks + r + i - 1) % 9) + 1 for i in range(5)]

    fd.append(np.concatenate(a, axis=1))

full_distances = np.concatenate(fd)

print("Part 2:", find_shortest_path(full_distances))
