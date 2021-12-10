with open("day6input.txt") as f:
    lines = f.readlines()

input_string = lines[0].strip()

input_list = [int(x) for x in input_string.split(",")]


def get_num_fish(number_days):
    buckets = [input_list.count(x) for x in range(0, 9)]

    for day in range(1, number_days + 1):
        zero_fish = buckets[0]

        for i in range(1, len(buckets)):
            buckets[i - 1] = buckets[i]
        buckets[8] = zero_fish
        buckets[6] += zero_fish

    return sum(buckets)


print(f"Part 1: {get_num_fish(80)}")
print(f"Part 2", get_num_fish(256))
