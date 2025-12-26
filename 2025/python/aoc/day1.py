def solve(text: str) -> int:
    position: int = 50

    parts: list[str] = text.split()
    count: int = 0
    for part in parts:
        part = turn_string_into_int(part)


        position: int = position + part
        position = position % 100
        if position == 0:
            count += 1

        print(position)
    return count

def turn_string_into_int(row: str) -> int:
    if row[0] == "R":
        muliplier = 1
    elif row[0] == "L":
        muliplier = -1
    else:
        raise Exception("Something went wrong")
    return muliplier*int(row[1:])


if __name__ == "__main__":
    from .harness import get_puzzle_input

    _input = get_puzzle_input(1)
    solution = solve(_input)
    print("---Solution---")
    print(solution)
    print("---END---")
