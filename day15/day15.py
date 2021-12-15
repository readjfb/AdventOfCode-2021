with open("day15input.txt") as f:
    data = f.read().strip()

distances = [[int(x) for x in line] for line in data.split("\n")]


class MyHeap:
    #  Heap where pop returns the element with the smallest value
    def __init__(self) -> None:
        self.heap = []
        self.heap_set = set()

    def push(self, value, item) -> None:
        upper_bound, lower_bound = len(self.heap) - 1, 0

        # Use binary search to find the correct position for insertion
        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2
            if self.heap[mid][0] > value:
                lower_bound = mid + 1
            else:
                upper_bound = mid - 1

        if item not in self.heap_set:
            self.heap.insert(lower_bound, (value, item))

            self.heap_set.add(item)

    def pop(self) -> tuple:
        v = self.heap.pop()
        self.heap_set.remove(v[1])

        return v


def find_shortest_path(distances) -> int:
    finalized = set()
    heap = MyHeap()
    heap.push(0, (len(distances[0]) - 1, len(distances) - 1))

    while heap.heap:
        value, item = heap.pop()

        if item == (0, 0):
            return value - distances[0][0] + distances[-1][-1]

        finalized.add(item)

        x, y = item

        for neighbor in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = neighbor
            nx = x + nx
            ny = y + ny
            if (
                len(distances) > ny >= 0
                and len(distances[0]) > nx >= 0
                and (nx, ny) not in finalized
            ):
                heap.push(distances[ny][nx] + value, (nx, ny))

    print("ERROR NO PATH FOUND!")
    return None


print("Part 1:", find_shortest_path(distances))

full_distances = [[0] * len(distances[0]) * 5 for _ in range(len(distances) * 5)]

for i in range(0, 5 * len(distances[0]), len(distances[0])):
    for j in range(0, 5 * len(distances), len(distances)):
        for k in range(len(distances[0])):
            for l in range(len(distances)):
                full_distances[i + k][j + l] = ((distances[k][l] - 1 + i + j) % 9) + 1

print("Part 2:", find_shortest_path(full_distances))
