from math import sqrt


def check_trial(dx0, dy0, target_x, target_y):
    x = 0
    y = 0

    dx, dy = dx0, dy0

    t = 0

    max_y_coord = 0

    while x <= target_x[1] and y >= target_y[0]:
        if target_x[0] <= x <= target_x[1] and target_y[0] <= y <= target_y[1]:
            return True, max_y_coord

        x += dx
        y += dy

        max_y_coord = max(y, max_y_coord)

        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1

        dy -= 1

        t += 1

    return False, y


def check_trial_fast(dx0, dy0, target_x, target_y):
    x = 0
    y = 0

    dx, dy = dx0, dy0

    while x <= target_x[1] and y >= target_y[0]:
        if target_y[0] <= y <= target_y[1] and target_x[0] <= x <= target_x[1]:
            return True

        x += dx
        y += dy

        if dx > 0:
            dx -= 1

        dy -= 1

    return False


def solve_part1(target_x, target_y):
    dx = int(sqrt(1 + 8 * target_x[0]) / 2)

    # Brute force to find y
    dy = max(
        dy
        for dy in range(target_y[0], 1000)
        if check_trial_fast(dx, dy, target_x, target_y)
    )

    return check_trial(dx, dy, target_x, target_y)[1]


def solve_part2(target_x, target_y):
    # Just straight up brute force the thing, with a *bit* of pruning
    possibles = 0

    for dx in range(int(sqrt(1 + 8 * target_x[0]) / 2), target_x[1] + 1):
        x = 0
        ddx = dx

        while x <= target_x[1] and ddx > 0:
            if target_x[0] <= x <= target_x[1]:
                break

            x += ddx
            ddx -= 1
        else:
            continue

        possibles += sum(
            check_trial_fast(dx, dy, target_x, target_y)
            for dy in range(target_y[0], 1000)
        )

    return possibles


if __name__ == "__main__":
    with open("day17input.txt") as f:
        input = f.read().strip()

    input = input.replace("target area: x=", "")
    input = input.split(", y=")

    input = [i.split("..") for i in input]

    input = [[int(i) for i in j] for j in input]

    print("Part 1:", solve_part1(input[0], input[1]))

    print("Part 2:", solve_part2(input[0], input[1]))
