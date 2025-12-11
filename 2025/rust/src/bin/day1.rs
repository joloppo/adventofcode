use aoc::harness;

fn main() {
    let day = harness::extract_day(file!());
    let input = harness::get_input(day);
    let mut counter = 0;
    let num_iterator = input.split_whitespace().map(|v| {
        let multiplier: i64 = match v.chars().nth(0).unwrap() {
            'L' => -1,
            'R' => 1,
            _ => panic!(),
        };
        let number = v[1..].parse::<i64>().unwrap();
        return multiplier * number;
    });
    num_iterator.clone().fold(50, |acc, x| {
        let new = (acc + x) % 100;
        if new == 0 {
            counter += 1;
        };
        return new;
    });
    dbg!(counter);
    counter = 0;
    num_iterator.clone().fold(50, |acc, x| {
        let new = acc + x;
        let mut new_count = ((new - 50).abs() + 50) / 100;
        println!("{} {} {} {}", acc, x, new, new_count);

        // from zero going left
        if new < 0 && acc == 0 {
            new_count -= 1;
        }
        counter += new_count;
        new.rem_euclid(100)
    });
    dbg!(counter);
}
