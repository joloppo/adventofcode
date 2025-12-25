from itertools import product


def solve(text: str) -> str:
    ranges, ids = parse_input(text)
    total = count_fresh(ranges, ids)
    total = count_ranges(ranges)

    return str(total)


def parse_input(text: str) -> tuple[list[range], list[int]]:
    ranges, ids = text.split("\n\n")
    ranges = ranges.split()
    ranges = [r.split("-") for r in ranges]
    assert all([len(r) == 2 for r in ranges])
    ranges = [range(int(a), int(b) + 1) for a, b in ranges]
    ids = [int(id) for id in ids.split()]
    return (ranges, ids)


def count_fresh(ranges: list[range], ids: list[int]) -> int:
    total = 0
    for id in set(ids):
        for range in ranges:
            if id in range:
                total += 1
                break
    return total


def count_ranges(ranges: list[range]) -> int:
    ranges_by_start = sorted(ranges, key=lambda r: r.start)
    active_range = ranges_by_start[0]
    total_len = 0
    start = active_range.start
    for next_range in ranges_by_start[1:]:
        if next_range.start > active_range.stop:
            # add range len + jump
            total_len += active_range.stop - start
            active_range = next_range
            start = active_range.start

        if next_range.stop > active_range.stop:
            active_range = next_range

    # close
    total_len += active_range.stop - start
    return total_len


if __name__ == "__main__":
    from .harness import day_from_filename, get_puzzle_input

    _input = get_puzzle_input(day_from_filename(__file__))
    solution = solve(_input)
    print("---Solution---")
    print(solution)
    print("---END---")


def test_1():
    _input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    solve(_input)
