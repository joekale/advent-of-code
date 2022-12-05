
fn main() {
    let contents = std::fs::read_to_string("/home/joe/dev/advent-of-code/2022/python/day1/input.txt")
        .expect("Should have been able to read the file");
    let trimmed = contents.trim_end();

    let str_loads: Vec<&str> = trimmed.split("\n\n").collect();
    let mut most: u32 = 0;
    for str_load in str_loads.iter() {
        let loads: Vec<&str> = str_load.split("\n").collect();
        let mut elf_load = 0;
        for load in loads.iter() {
            elf_load += load.parse::<u32>().unwrap();
        }
        if elf_load > most {
            most = elf_load;
        }
    }
    println!("{:?}", most)
}
