def solve(text: str) -> str:
    parsed = split_parse(text)
    current_value = 50
    current_counter = 0
    for v in parsed:
        # current_value, current_counter = advance(current_value, current_counter, v)
        current_value, current_counter = advance_part2(
            current_value, current_counter, v
        )
    return str(current_counter)


def split_parse(text: str) -> list[int]:
    lines = text.split()
    out = []
    for line in lines:
        if not line:
            continue
        if line.startswith("L"):
            out.append(-(int(line[1:])))
            continue
        if line.startswith("R"):
            out.append(+(int(line[1:])))
            continue
        raise ValueError(f"Unexpected input: {line}")
    return out


def advance(current_value: int, counter: int, lr_value: int) -> tuple[int, int]:
    """returns new current value and new counter"""
    current_value += lr_value
    current_value = current_value % 100
    if current_value == 0:
        counter += 1
    return current_value, counter


def advance_part2(current_value: int, counter: int, lr_value: int) -> tuple[int, int]:
    """returns new current value and new counter"""
    new_value = current_value + lr_value
    new_count = (abs(new_value - 50) + 50) // 100

    # from zero going left
    if new_value < 0 and current_value == 0:
        new_count -= 1

    counter += new_count
    new_value = new_value % 100

    return new_value, counter


if __name__ == "__main__":
    from .harness import day_from_filename, get_puzzle_input

    _input = get_puzzle_input(day_from_filename(__file__))
    solution = solve(_input)
    print("---Solution---")
    print(solution)
    print("---END---")
