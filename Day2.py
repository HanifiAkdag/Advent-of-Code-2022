def part1():
    point = 0
    with open('data/day2input.txt') as f:
        for line in f:
            if not line:
                break
            elf_shape = line[0]
            your_shape = line[2]

            if your_shape == 'X':
                point += 1
                if elf_shape == 'C':
                    point += 6
            
            elif your_shape == 'Y':
                point += 2
                if elf_shape == 'A':
                    point += 6

            else:
                point += 3
                if elf_shape == 'B':
                    point += 6

            if ord(your_shape) - ord(elf_shape) == 23:
                point += 3
    return point

def part2():
    point = 0
    with open('data/day2input.txt') as f:
        for line in f:
            if not line:
                break
            elf_shape = line[0]
            outcome = line[2]

            if outcome == 'Z':
                point += 6
                if elf_shape == 'A':
                    point += 2
                elif elf_shape == 'B':
                    point += 3
                else:
                    point += 1
            elif outcome == 'Y':
                point += 3
                if elf_shape == 'A':
                    point += 1
                elif elf_shape == 'B':
                    point += 2
                else:
                    point += 3
            else:
                if elf_shape == 'A':
                    point += 3
                elif elf_shape == 'B':
                    point += 1
                else:
                    point += 2
    
    return point 

print(part1())
print(part2())