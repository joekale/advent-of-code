use std::{fs, collections::HashMap, usize::MAX};

fn main() {
    let contents = fs::read_to_string("full_input.txt")
        .expect("Should have been able to read the file");
    let res_p1: usize = contents.lines().map(String::from).map(part1_string_to_calibration).sum();
    println!("Part 1 Answer: {}", res_p1);
    let res_p2: usize = contents.lines().map(String::from).map(part2_string_to_calibration).sum();
    println!("Part 2 Answer: {}", res_p2);
}


fn part1_string_to_calibration(line: String) -> usize {
    let mut first = 10;
    let mut second = 0;
    for ch in line.chars() {
        if first > 9 && ch.is_numeric() {
            first = ch.to_digit(10).ok_or("Failed to parse digit").unwrap();
            second = ch.to_digit(10).ok_or("Failed to parse digit").unwrap();
        } else if first < 10 && ch.is_numeric() {
            second = ch.to_digit(10).ok_or("Failed to parse digit").unwrap();
        }
    }

    let res = usize::try_from((first * 10) + second).unwrap();
    return res;
}

fn part2_string_to_calibration(line: String) -> usize {
    let hmap = HashMap::from([("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5),
                                                  ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9)]);
    
    let mut first = 0;
    let mut second = 0;

    let mut first_num_pos: usize = MAX;
    let mut last_num_pos: usize = 0;

    for (spelled, num) in hmap {
        match line.find(&num.to_string()) {
            Some(val) => {
                if val < first_num_pos {
                    first_num_pos = val;
                    first = num;
                }
            },
            _ => {}
        }
        match line.rfind(&num.to_string()) {
            Some(val) => {
                if val >= last_num_pos {
                    last_num_pos = val;
                    second = num;
                }
            },
            _ => {}
        }
        match line.find(&spelled) {
            Some(val) => {
                if val < first_num_pos {
                    first_num_pos = val;
                    first = num;
                }
            },
            _ => {}
        }
        match line.rfind(&spelled) {
            Some(val) => {
                if val >= last_num_pos {
                    last_num_pos = val;
                    second = num;
                }
            },
            _ => {}
        }
    }

    let res = usize::try_from((first * 10) + second).unwrap();
    return res;
}