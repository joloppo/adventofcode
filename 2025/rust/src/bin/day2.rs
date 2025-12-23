use aoc::harness;
use itertools::Itertools;

fn main() {
    let day = harness::extract_day(file!());
    let input = harness::get_input(day);
    let pairs = input
        .trim()
        .split(',')
        .filter(|v| !v.is_empty())
        .map(|v| -> (usize, usize) {
            v.split('-')
                .map(|v| v.parse::<usize>().unwrap())
                .collect_tuple::<(usize, usize)>()
                .unwrap()
        })
        .collect::<Vec<(usize, usize)>>();

    let mut counter = 0;
    for (a, b) in pairs.clone() {
        for n in a..=b {
            let int_as_string = n.to_string();
            let half = int_as_string.len() / 2;
            if half * 2 != int_as_string.len() {
                continue;
            }
            if int_as_string[..half] == int_as_string[half..] {
                counter += n;
            }
        }
    }
    dbg!(counter);

    let mut counter = 0;
    for (a, b) in pairs {
        for n in a..=b {
            let int_as_string = n.to_string();
            let half = int_as_string.len() / 2;
            for ix in 1..=half {
                let mult = int_as_string.len() / ix;
                if int_as_string[..ix].repeat(mult) == int_as_string {
                    counter += n;
                    break;
                }
            }
        }
    }
    dbg!(counter);
}
