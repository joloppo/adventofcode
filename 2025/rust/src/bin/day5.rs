use itertools::Itertools;
use std::ops::RangeInclusive;

use aoc::harness;

fn main() {
    let day = harness::extract_day(file!());
    let input = harness::get_input(day);
    let (ranges, ids) = parse_input(input);

    let a1 = ids_in_ranges(ids, ranges.clone());
    let a2 = total_range_sizes(ranges);
    dbg!(a1, a2);
}

fn parse_input(input: String) -> (Vec<RangeInclusive<usize>>, Vec<usize>) {
    let mut parts = input.split("\n\n");
    let p1 = parts.next();
    let ranges = p1
        .unwrap()
        .split_whitespace()
        .map(|r| {
            r.split("-")
                .map(|v| v.parse::<usize>().unwrap())
                .collect_tuple::<(usize, usize)>()
                .unwrap()
        })
        .map(|tup| tup.0..=tup.1)
        .collect();

    let ids = parts
        .next()
        .unwrap()
        .split_whitespace()
        .map(|v| v.parse::<usize>().unwrap())
        .collect();

    return (ranges, ids);
}

fn ids_in_ranges(ids: Vec<usize>, ranges: Vec<RangeInclusive<usize>>) -> usize {
    let mut counter = 0;
    'id_loop: for id in ids.iter() {
        for range in ranges.iter() {
            if range.contains(id) {
                counter += 1;
                continue 'id_loop;
            }
        }
    }
    return counter;
}

fn total_range_sizes(mut ranges: Vec<RangeInclusive<usize>>) -> usize {
    let mut total = 0;
    ranges.sort_by(|v1, v2| v1.start().cmp(v2.start()));
    let mut current_start = ranges[0].start();
    let mut current_end = ranges[0].end();
    for range in ranges.iter().skip(1) {
        if current_end < range.start() {
            total += current_end - current_start + 1;
            current_start = range.start();
            current_end = range.end();
        }
        if range.end() > current_end {
            current_end = range.end();
        }
    }
    // last one
    total += current_end - current_start + 1;
    return total;
}
