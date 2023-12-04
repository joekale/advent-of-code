use std::{fs};

fn main() {
    let contents = fs::read_to_string("full_input.txt")
        .expect("Should have been able to read the file");
    let res_p1: usize = contents.lines().map(String::from).map(part1).sum();
    println!("Part 1 Answer: {}", res_p1);
    let res_p2: usize = contents.lines().map(String::from).map(part2).sum();
    println!("Part 2 Answer: {}", res_p2);
}

fn part2(line: String) -> usize {
    let game_details: Vec<&str> = line.split(":").collect();
    let mut min_red = 0;
    let mut min_green = 0;
    let mut min_blue = 0;

    for game in game_details[1].split(";").collect::<Vec<&str>>() {
        for color in game.split(",").collect::<Vec<&str>>() {
            let num_color: Vec<&str> = color.trim().split(" ").collect();
            let num = i32::from_str_radix(num_color[0], 10).unwrap();
            match num_color[1] {
                "red" => if num > min_red {
                    min_red = num;
                },
                "blue" => if num > min_blue {
                    min_blue = num;
                },
                "green" => if num > min_green {
                    min_green = num;
                },
                _ => {}

            }
        }
    }
                                                 
    return usize::try_from(min_red * min_green * min_blue).unwrap();
}


fn part1(line: String) -> usize {
    let game_details: Vec<&str> = line.split(":").collect();
    let game_id = usize::from_str_radix(&game_details[0].chars()
                                                                .filter(|ch| ch.is_numeric())
                                                                .collect::<String>(), 10)
                                                                .unwrap();
    for game in game_details[1].split(";").collect::<Vec<&str>>() {
        for color in game.split(",").collect::<Vec<&str>>() {
            let number = usize::from_str_radix(&color.chars()
                                                                .filter(|ch| ch.is_numeric())
                                                                .collect::<String>(), 10)
                                                                .unwrap();
            if color.ends_with("red") && number > 12 {
                return 0;
            } else if color.ends_with("green") && number > 13 {
                return 0;
            } else if color.ends_with("blue") && number > 14 {
                return 0;
            }
        }
    }
                                                                        
    return game_id;
}