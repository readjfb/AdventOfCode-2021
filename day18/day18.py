import copy

# This essentially operates in tree form. It's a bit of a mess, but it works


def has_nested_depth(str_num, target_depth):
    depth = 0

    for i in str_num:
        if i == "[":
            depth += 1
        elif i == "]":
            depth -= 1

        if depth == target_depth + 1:
            return True

    return False


def has_number_gtt(str_num, target):
    str_num = str_num.replace("[", "").replace("]", "")

    return any(int(i) > target for i in str_num.split(", "))


def perform_explode(num, curr_depth=0):
    # A pair that is 5 deep is exploded in num
    # Pair's left value is added to the regular number to it's left
    # Pair's right value is added to the regular number to it's right

    # First, find the pair to target
    if not isinstance(num, list):
        return None, None, None

    if curr_depth == 4:
        return num[0], num[1], False

    ind = None
    for i, val in enumerate(num):
        left, right, done = perform_explode(val, curr_depth + 1)

        if left is not None or right is not None:
            ind = i

            if not done:
                num[i] = 0

            break

    if left and ind > 0:
        v = num
        i = ind - 1

        if not isinstance(v[i], int):
            while not isinstance(v[i], int):
                v = v[i]
                i = -1

        v[i] += left
        left = 0

    if right and ind < len(num) - 1:
        v = num
        i = ind + 1

        if not isinstance(v[i], int):
            while not isinstance(v[i], int):
                v = v[i]
                i = 0

        v[i] += right
        right = 0

    return left, right, True


def perform_split(num, done=False):
    # leftmost number splits into two numbers
    if isinstance(num, int):
        return num >= 10, False

    for i, val in enumerate(num):
        go, done = perform_split(val, done)

        if done:
            return False, True

        if go:
            num[i] = [int(val / 2), int((val / 2) + 0.5)]
            return False, True

    return False, done


def add_numbers(num1, num2):
    num1 = copy.deepcopy(num1)
    num2 = copy.deepcopy(num2)

    done = False

    num = [num1, num2]

    while not done:
        str_num = str(num)
        if has_nested_depth(str_num, 4):
            perform_explode(num)
        elif has_number_gtt(str_num, 9):
            perform_split(num)
        else:
            done = True

    return num


def calculate_magnitude(num):
    if isinstance(num, int):
        return num

    return 3 * calculate_magnitude(num[0]) + 2 * calculate_magnitude(num[1])


# Tests for explode
"""
test1 = [[[[[9, 8], 1], 2], 3], 4]
perform_explode(test1)

test2 = [7, [6, [5, [4, [3, 2]]]]]
perform_explode(test2)

test3 = [[6, [5, [4, [3, 2]]]], 1]
perform_explode(test3)

test4 = [[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]
perform_explode(test4)

test5 = [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]
perform_explode(test5)

test6 = [[1, [[[3, 4], 4], 5]], 1]
perform_explode(test6)

test7 = [[[1, 1], [[[3, 4], 4], 5]], 1]
perform_explode(test7)

assert test1 == [[[[0, 9], 2], 3], 4]
assert test2 == [7, [6, [5, [7, 0]]]]
assert test3 == [[6, [5, [7, 0]]], 3]
assert test4 == [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]
assert test5 == [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]
assert test6 == [[4, [[0, 8], 5]], 1]
assert test7 == [[[1, 4], [[0, 8], 5]], 1]
"""

# Things that are ran start here

with open("day18input.txt") as f:
    data = f.read().strip()

lines = []
b = None
for line in data.split("\n"):
    exec("b=" + line)
    lines.append(b)

# Part 1
result = lines[0]
for line in lines[1:]:
    result = add_numbers(result, line.copy())

print("Part 1:", calculate_magnitude(result))

# Part 2
# Find the largest magnitude of adding two numbers
largest = 0
for i, line1 in enumerate(lines[:-1]):
    for line2 in lines[i + 1 :]:
        result = add_numbers(line1, line2)
        largest = max(largest, calculate_magnitude(result))

        result = add_numbers(line2, line1)
        largest = max(largest, calculate_magnitude(result))

print("Part 2:", largest)
