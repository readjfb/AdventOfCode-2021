import numpy as np

# I feel like there should be a really elegant solution to this problem,
# but I could only come up with the brute force solution.
# Luckily, the given problem doesn't require many iterations.

with open("day11input.txt") as f:
    lines = f.readlines()

octopus_matrix = []

for line in lines:
    octopus_matrix.append([int(x) for x in line.strip()])

# Convert to numpy array
octopus_matrix = np.array(octopus_matrix, dtype=int)
octopus_matrix_copy = octopus_matrix.copy()

ones = np.ones(octopus_matrix.shape, dtype=int)

# Perform one step of the algorithm
def one_step(matrix):
    matrix += ones

    flashed = np.zeros(matrix.shape, dtype=bool)

    indices = np.where(matrix > 9)
    indices = [(x, y) for x, y in zip(indices[0], indices[1]) if not flashed[x, y]]

    while indices:
        for x, y in indices:
            matrix[x, y] = 0

            flashed[x, y] = True

            # Increment the values of the neighbours, without going out of range or repeating
            neighbors = [
                (x, y + 1),
                (x + 1, y + 1),
                (x + 1, y),
                (x + 1, y - 1),
                (x, y - 1),
                (x - 1, y - 1),
                (x - 1, y),
                (x - 1, y + 1),
            ]

            for nx, ny in neighbors:
                if 0 <= nx < matrix.shape[0] and 0 <= ny < matrix.shape[1]:
                    matrix[nx, ny] += 1

        indices = np.where(matrix > 9)
        indices = [(x, y) for x, y in zip(indices[0], indices[1]) if not flashed[x, y]]

    flashed_indices = np.where(flashed == True)

    matrix[flashed_indices] = 0
    return len(flashed_indices[0])


p1_sum = 0
num_steps = 100
for i in range(num_steps):
    p1_sum += one_step(octopus_matrix)

full_size = octopus_matrix.shape[0] * octopus_matrix.shape[1]
day = 1
while one_step(octopus_matrix_copy) != full_size:
    day += 1

print("Part 1:", p1_sum)
print("Part 2:", day)
