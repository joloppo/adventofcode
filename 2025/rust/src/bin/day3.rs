use aoc::harness;

fn main() {
    let day = harness::extract_day(file!());
    let input = harness::get_input(day);
    let joltages = input.split_whitespace().map(max_line_for_joltage);
    let result: usize = joltages.sum();
    dbg!(result);
}

fn max_line_for_joltage(input: &str) -> usize {
    const N_DIGITS: usize = 12;
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
        dbg!(exponent);
        total += 10_usize.pow(exponent as u32) * (*max_value as usize);
    }
    dbg!(input, total);
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

/*
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
*/

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        let input = "987654321111111";
        let output = max_line_for_joltage(input);
        assert_eq!(output,);
    }

    #[test]
    fn test_bad_add() {
        // This assert would fire and test will fail.
        // Please note, that private functions can be tested too!
        assert_eq!(bad_add(1, 2), 3);
    }
}
