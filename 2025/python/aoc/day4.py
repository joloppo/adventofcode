from itertools import product

BoolMatrix = list[list[bool]]


def solve(text: str) -> str:
    boolified = boolify(text)
    padded = pad(boolified)
    total_viable = count_part2(padded)
    return str(total_viable)


def boolify(text: str) -> BoolMatrix:
    lines = text.split()
    lines = [[c == "@" for c in l] for l in lines]
    return lines


def pad(bools: BoolMatrix) -> BoolMatrix:
    line_len = len(bools[0])
    first_last_line = [False] * (line_len + 2)
    bools = [[False] + line + [False] for line in bools]
    return [first_last_line] + bools + [first_last_line]


def count(bools: BoolMatrix) -> int:
    targets = [(x, y) for x, y in product((+1, 0, -1), (+1, 0, -1))]
    targets.remove((0, 0))
    middle_start = (1, 1)
    iter_x = len(bools[0]) - 2
    iter_y = len(bools) - 2
    total_viable = 0
    for y in range(iter_y):
        for x in range(iter_x):
            middle = (middle_start[0] + x, middle_start[0] + y)
            if not bools[middle[1]][middle[0]]:
                continue
            n_rolls = 0
            for x_t, y_t in targets:
                point = (middle[0] + x_t, middle[1] + y_t)
                if bools[point[1]][point[0]]:
                    n_rolls += 1
            if n_rolls < 4:
                total_viable += 1
    return total_viable


def count_part2(bools: BoolMatrix) -> int:
    targets = [(x, y) for x, y in product((+1, 0, -1), (+1, 0, -1))]
    targets.remove((0, 0))
    middle_start = (1, 1)
    iter_x = len(bools[0]) - 2
    iter_y = len(bools) - 2
    total_viable = 0
    while True:
        viable_iteration = 0
        points_to_remove = []
        for y in range(iter_y):
            for x in range(iter_x):
                middle = (middle_start[0] + x, middle_start[0] + y)
                if not bools[middle[1]][middle[0]]:
                    continue
                n_rolls = 0
                for x_t, y_t in targets:
                    point = (middle[0] + x_t, middle[1] + y_t)
                    if bools[point[1]][point[0]]:
                        n_rolls += 1
                if n_rolls < 4:
                    viable_iteration += 1
                    points_to_remove.append(middle)
        if viable_iteration == 0:
            break
        for point in points_to_remove:
            bools[point[1]][point[0]] = False
        total_viable += viable_iteration

    return total_viable


if __name__ == "__main__":
    from .harness import get_puzzle_input

    _input = get_puzzle_input(4)
    solution = solve(_input)
    print("---Solution---")
    print(solution)
    print("---END---")


def test_1():
    input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    assert solve(input) == str(13)
