use aoc::harness;
use itertools::Itertools;

fn main() {
    let day = harness::extract_day(file!());
    let input = harness::get_input(day);
    let bools = str_to_array(&input);
    let resultx = iter_bools(bools.clone());

    let mut total = 0;
    let mut input = bools.clone();
    loop {
        let result = iter_bools(input);
        input = result.0;
        total += result.1;
        if result.1 == 0 {
            dbg!(array_to_str(input));
            break;
        }
    }
    dbg!(resultx.1);
    dbg!(total);
}

fn str_to_array(input: &str) -> Vec<Vec<bool>> {
    input
        .split_whitespace()
        .map(|r| r.chars().map(|c| c == '@').collect())
        .collect()
}
fn array_to_str(input: Vec<Vec<bool>>) -> String {
    input
        .into_iter()
        .map(|row| row.into_iter().map(|b| if b { '@' } else { '.' }).collect::<String>())
        .collect::<Vec<_>>()
        .join("\n")
}

fn iter_bools(input: Vec<Vec<bool>>) -> (Vec<Vec<bool>>, usize) {
    let mut count = 0;
    let arround_mask: Vec<(isize, isize)> = vec![(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)];
    let y_size = input.len();
    let x_size = input[0].len();
    let mut new_vec = vec![vec![false; x_size]; y_size];

    'cell_loop: for (x, y) in (0..x_size).cartesian_product(0..y_size) {
        let mut surrounding = 0;
        let cell: bool = input.get(y).and_then(|row| row.get(x)).copied().unwrap_or(false);
        if !cell {
            continue;
        }

        for mask_target in arround_mask.iter() {
            if *input
                .get((y as isize + mask_target.1) as usize)
                .and_then(|v| v.get((x as isize + mask_target.0) as usize))
                .unwrap_or(&false)
            {
                surrounding += 1;
            }
            if surrounding >= 4 {
                new_vec[y][x] = true;
                continue 'cell_loop;
            }
        }
        count += 1;
    }

    return (new_vec, count);
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::{fixture, rstest};

    #[fixture]
    fn array_as_str() -> &'static str {
        return "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@";
    }
    #[fixture]
    fn array_as_bools() -> Vec<Vec<bool>> {
        return vec![
            vec![false, false, true, true, false, true, true, true, true, false],
            vec![true, true, true, false, true, false, true, false, true, true],
            vec![true, true, true, true, true, false, true, false, true, true],
        ];
    }

    #[rstest]
    fn test_str_to_array(array_as_str: &'static str, array_as_bools: Vec<Vec<bool>>) {
        assert_eq!(str_to_array(array_as_str), array_as_bools);
    }

    #[rstest]
    fn test_array_to_str(array_as_str: &'static str, array_as_bools: Vec<Vec<bool>>) {
        assert_eq!(array_to_str(array_as_bools), array_as_str);
    }
}
