
elf_load = 0
elf_loads = {}
for line in io.lines("/home/joe/dev/advent-of-code/2022/python/day1/input.txt") do
    if line ~= '' then
	elf_load = elf_load + tonumber(line)
    else
	table.insert(elf_loads, elf_load)
	elf_load = 0
    end
end
table.sort(elf_loads)

answer = elf_loads[#elf_loads - 2] + elf_loads[#elf_loads - 1] + elf_loads[#elf_loads]

print(answer)
