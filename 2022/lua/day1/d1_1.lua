
most = 0
elf_load = 0
for line in io.lines("/home/joe/dev/advent-of-code/2022/python/day1/input.txt") do
    if line ~= '' then
	elf_load = elf_load + tonumber(line)
    else
	if elf_load > most then
	    most = elf_load
	end
	elf_load = 0
    end
    print(elf_load)
end
print(most)
