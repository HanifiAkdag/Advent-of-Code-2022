def part1():  
    with open('data/day6input.txt') as f:
        s = f.readline()

    for i in range(len(s) - 3):
        tmp = s[i:i+4]
        if len(set(tmp)) == 4:
            return i + 4


def part2():  
    with open('data/day6input.txt') as f:
        s = f.readline()

    for i in range(len(s) - 3):
        tmp = s[i:i+14]
        if len(set(tmp)) == 14:
            return i + 14


print(part1())
print(part2())