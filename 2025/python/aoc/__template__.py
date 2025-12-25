def solve(text: str) -> str:
    return text


if __name__ == "__main__":
    from .harness import day_from_filename, get_puzzle_input

    _input = get_puzzle_input(day_from_filename(__file__))
    solution = solve(_input)
    print("---Solution---")
    print(solution)
    print("---END---")
