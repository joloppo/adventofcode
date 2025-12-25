import math


def solve(text: str) -> str:
    columns, instructions = parse_input_part2(text)
    total = calculate(columns, instructions)
    return total


def parse_input(text: str) -> tuple[list[list[int]], list[str]]:
    lines = text.splitlines()
    instructions = lines[-1].split()
    numbers = [[int(n) for n in line.split()] for line in lines[:-1] if len(line) > 0]
    columns = list(zip(*numbers))

    return columns, instructions


def calculate(columns: list[list[int]], instructions: list[str]) -> int:
    instruction_funcs = [
        math.prod if instruction == "*" else sum for instruction in instructions
    ]
    total = 0
    for column, instruction in zip(columns, instruction_funcs):
        total += instruction(column)
    return total


def int_convert(_tuple: tuple) -> int | None:
    _str = "".join(_tuple)
    if not _str.strip():
        return None
    else:
        return int(_str.strip())


def parse_input_part2(text: str) -> tuple[list[list[int]], list[str]]:
    lines = text.splitlines()
    instructions = lines[-1].split()
    lines = lines[:-1]
    lines = list(filter(lambda x: bool(x.strip()), lines))
    max_len = max([len(line) for line in lines])
    lines = [line.ljust(max_len) for line in lines]
    charzipped = list(zip(*lines))
    numbers = [int_convert(_tuple) for _tuple in charzipped]
    split_numbers = []
    in_split = True
    for number in numbers:
        if in_split:
            if number is not None:
                split_numbers.append(list())
                split_numbers[-1].append(number)
                in_split = False
            else:
                continue
        else:
            if number is not None:
                split_numbers[-1].append(number)
            else:
                in_split = True
    return split_numbers, instructions


if __name__ == "__main__":
    from .harness import day_from_filename, get_puzzle_input

    _input = get_puzzle_input(day_from_filename(__file__))
    solution = solve(_input)
    print("---Solution---")
    print(solution)
    print("---END---")


def test_int_convert():
    assert None == int_convert((" ", " "))


def test_1():
    input = """
    123 328  51 64
     45 64  387 23
      6 98  215 314
    *   +   *   +  """
    r = parse_input(input)
    r = calculate(r[0], r[1])
    assert r == 4277556


def test_2():
    input = """
    123 328  51 64
     45 64  387 23
      6 98  215 314
    *   +   *   +  """
    r = parse_input_part2(input)
    r = calculate(r[0], r[1])
    assert r == 3263827
