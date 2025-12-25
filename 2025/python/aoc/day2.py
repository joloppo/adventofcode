Range = tuple[int, int]


def solve1(text: str) -> str:
    ranges = split_parse(text)
    double_ids_total = 0
    for start, stop in ranges:
        for n in range(start, stop + 1):
            str_num = str(n)
            str_num_len = len(str_num)
            if len(str_num) % 2 != 0:
                continue
            if str_num[0 : int(str_num_len / 2)] == str_num[int(str_num_len / 2) :]:
                double_ids_total += n
    return str(double_ids_total)


def solve2(text: str) -> str:
    ranges = split_parse(text)
    double_ids_total = 0
    for start, stop in ranges:
        for n in range(start, stop + 1):
            str_num = str(n)
            str_num_len = len(str_num)
            _ids = set()
            for size in range(1, int(str_num_len / 2) + 1):
                if (str_num_len % size) != 0:
                    continue
                if str_num[:size] * int(str_num_len / size) == str_num:
                    _ids |= {n}
            double_ids_total += sum(_ids)

    return str(double_ids_total)


def split_parse(text: str) -> list[Range]:
    ranges = text.split(",")
    ranges = [range.split("-") for range in ranges]
    ranges = [(int(start), int(stop)) for start, stop in ranges]
    return ranges


if __name__ == "__main__":
    from .harness import day_from_filename, get_puzzle_input

    _input = get_puzzle_input(day_from_filename(__file__))
    solution = solve2(_input)
    print("---Solution---")
    print(solution)
    print("---END---")
