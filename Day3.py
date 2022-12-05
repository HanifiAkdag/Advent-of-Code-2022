def part1():
    total = 0

    with open('data/day3input.txt') as f:
        for line in f:
            rucksack = line.strip()
            middle = int(len(rucksack) / 2)
            first = rucksack[:middle]
            second = rucksack[middle:]

            s = set(first)
            for char in second:
                if char in s:
                    if char.isupper():
                        total += ord(char) - 38
                    else:
                        total += ord(char) - 96
                    break

    return total

def part2():
    total = 0

    with open('data/day3input.txt') as f:
        group = []
        for line in f:
            group.append(line.strip())
            if len(group) % 3 != 0:
                continue
            else:
                badge = set(group[0]).intersection(group[1]).intersection(group[2]).pop()
                group.clear()
                if badge.isupper():
                    total += ord(badge) - 38
                else:
                    total += ord(badge) - 96
    return total

print(part1())
print(part2())