with open("day15input.txt") as f:
    data = f.read().strip()

risks = [[int(x) for x in line] for line in data.split("\n")]


class MyHeap:
    #  Heap where pop returns the element with the smallest value
    def __init__(self) -> None:
        self.heap = []

    def push(self, value, item) -> None:
        upper_bound =  len(self.heap) - 1
        lower_bound = 0

        # Use binary search to find the correct position for insertion
        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2
            if self.heap[mid][0] > value:
                lower_bound = mid + 1
            else:
                upper_bound = mid - 1

        self.heap.insert(lower_bound, (value, item))

    def pop(self) -> tuple:
        return self.heap.pop()


def find_shortest_path(risks) -> int:
    finalized = set()
    heap = MyHeap()
    heap.push(0, (len(risks[0]) - 1, len(risks) - 1))

    while heap.heap:
        value, item = heap.pop()

        if item == (0, 0):
            return value - risks[0][0] + risks[-1][-1]

        if item in finalized:
            continue

        finalized.add(item)

        x, y = item

        for neigh in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
            if (
                len(risks) > neigh[1] >= 0
                and len(risks[0]) > neigh[0] >= 0
                and neigh not in finalized
            ):
                heap.push(risks[neigh[1]][neigh[0]] + value, neigh)

    print("ERROR NO PATH FOUND!")
    return None


print("Part 1:", find_shortest_path(risks))

full_distances = [[0] * len(risks[0]) * 5 for _ in range(len(risks) * 5)]

for i in range(0, 5 * len(risks[0]), len(risks[0])):
    for j in range(0, 5 * len(risks), len(risks)):
        for k in range(len(risks[0])):
            for l in range(len(risks)):
                full_distances[i + k][j + l] = ((risks[k][l] - 1 + i + j) % 9) + 1

print("Part 2:", find_shortest_path(full_distances))
