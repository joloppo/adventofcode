use aoc::harness;

const N_DIGITS: usize = 12;

fn main() {
    let day = harness::extract_day(file!());
    let input = harness::get_input(day);
    let joltages = input.split_whitespace().map(max_line_for_joltage);
    let result: usize = joltages.sum();
    dbg!(result);
}

fn max_line_for_joltage(input: &str) -> usize {
    let as_digits = input
        .chars()
        .filter_map(|v| v.to_digit(10))
        .collect::<Vec<u32>>();
    let mut total = 0;

    let mut current_ix = 0;
    for ix in 0..N_DIGITS {
        let (max_ix, max_value) = as_digits[current_ix + ix..=input.len() - (N_DIGITS - ix)]
            .first_max()
            .unwrap();
        current_ix += max_ix;
        let exponent = N_DIGITS - ix - 1;
        total += 10_usize.pow(exponent as u32) * (*max_value as usize);
    }
    return total;
}

trait FirstMax {
    type Item;
    fn first_max(&self) -> Option<(usize, &Self::Item)>;
}

impl<U: Ord> FirstMax for [U] {
    type Item = U;
    fn first_max(&self) -> Option<(usize, &U)> {
        if self.is_empty() {
            return None;
        }
        let mut best_idx = 0;
        let mut best_val = &self[0];

        for (i, v) in self.iter().enumerate().skip(1) {
            if v > best_val {
                // “>” keeps the first max
                best_idx = i;
                best_val = v;
            }
        }
        Some((best_idx, best_val))
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case(987654321111111, 987654321111)]
    #[case(811111111111119, 811111111119)]
    #[case(234234234234278, 434234234278)]
    #[case(818181911112111, 888911112111)]
    fn test1(#[case] input: usize, #[case] expected: usize) {
        let input = input.to_string();
        let output = max_line_for_joltage(&input);
        assert_eq!(output, expected);
    }
}
