import math


def solve(text: str) -> str:
    columns, instructions = parse_input(text)
    total = calculate(columns, instructions)
    return total


def parse_input(text: str) -> tuple[list[list[int]], list[str]]:
    lines = text.splitlines()
    instructions = lines[-1].split()
    numbers = "".join(lines[:-1]).split()
    numbers = [int(n) for n in numbers]
    columns = [
        numbers[ix :: len(numbers) // len(instructions)]
        for ix in range(len(instructions))
    ]

    return columns, instructions


def calculate(columns: list[list[int]], instructions: list[str]) -> int:
    instruction_funcs = [
        math.prod if instruction == "*" else sum for instruction in instructions
    ]
    total =
    for column, instruction in zip(columns, instruction_funcs):
        total += instruction(column)
    return total


if __name__ == "__main__":
    from .harness import get_puzzle_input

    _input = get_puzzle_input(6)
    solution = solve(_input)
    print("---Solution---")
    print(solution)
    print("---END---")


def test_1():
    input = """
    123 328  51 64
     45 64  387 23
      6 98  215 314
    *   +   *   +  """
    r = parse_input(input)
    print(r)
