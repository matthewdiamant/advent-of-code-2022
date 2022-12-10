fn solve_part_1(_input: &Vec<char>) -> i64 {
    return 0;
}

static INPUT: &str = include_str!("input.txt");
fn main() {
    let input: Vec<char> = INPUT.lines().map(|x| x.parse().unwrap()).collect();
    println!("{}", solve_part_1(&input));
}
