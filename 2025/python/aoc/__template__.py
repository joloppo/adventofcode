def solve(text: str) -> str:
    return text


if __name__ == "__main__":
    from .harness import get_puzzle_input

    _input = get_puzzle_input(1)
    solution = solve(_input)
    print("---Solution---")
    print(solution)
    print("---END---")
