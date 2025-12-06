def solve(text: str) -> str:
    lines = text.split()
    max_joltages = [max_joltage_for_line_part2(l) for l in lines]
    total = sum(max_joltages)

    return str(total)


def max_joltage_for_line(line: str) -> int:
    ints = [int(c) for c in line]
    first_digit = max(ints[:-1])
    first_digit_index = ints.index(first_digit)
    second_digit = max(ints[first_digit_index + 1 :])
    return first_digit * 10 + second_digit


N_DIGITS = 12


def max_joltage_for_line_part2(line: str) -> int:
    ints = [int(c) for c in line]
    len_line = len(ints)

    current_index = 0
    digits = []

    for digit in range(1, N_DIGITS + 1):
        n_digits_left_to_do = N_DIGITS - digit
        viable_part_of_line = ints[current_index : len_line - n_digits_left_to_do]
        first_digit = max(viable_part_of_line)
        current_index += viable_part_of_line.index(first_digit) + 1
        digits.append(str(first_digit))

    total = int("".join(digits))
    return total


if __name__ == "__main__":
    from .harness import get_puzzle_input

    _input = get_puzzle_input(3)
    solution = solve(_input)
    print("---Solution---")
    print(solution)
    print("---END---")


def test_1():
    input = "987654321111111"
    result = solve(input)
    assert result == str(987654321111)


def test_2():
    input = "811111111111119"
    result = solve(input)
    assert result == str(811111111119)


def test_3():
    input = "234234234234278"
    assert solve(input) == str(434234234278)


def test_4():
    input = "818181911112111"
    assert solve(input) == str(888911112111)
