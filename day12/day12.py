class Cave:
    def __init__(self, id, large) -> None:
        self.id = id
        self.children = []
        self.large = large


with open("day12input.txt") as f:
    lines = f.readlines()

cut_lines = [line.strip().split("-") for line in lines]
combined = [set(item) for item in cut_lines]
combined = set().union(*combined)

cave_ids = {cave: Cave(cave, cave.upper() == cave) for cave in combined}

for line in cut_lines:
    cave_ids[line[0]].children.append(cave_ids[line[1]])
    cave_ids[line[1]].children.append(cave_ids[line[0]])


def turtle(cave, visited, twice) -> list:
    return_list = []
    visited.append(cave.id)

    if cave == cave_ids["end"]:
        return [visited] + return_list

    for child in cave.children:
        if child.large or child.id not in visited:
            return_list += turtle(child, visited[:], twice)
        elif not twice and child != cave_ids["start"]:
            return_list += turtle(child, visited[:], True)

    return return_list


paths1 = turtle(cave_ids["start"], [], True)
print("Part 1:", len(paths1))

paths2 = turtle(cave_ids["start"], [], False)
print("Part 2:", len(paths2))
