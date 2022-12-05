def part1():
    curr_deer = 0
    deers = []
    with open('data/day1input.txt') as f:
        for line in f:
            line = line.strip()
            if line == "":
                deers.append(curr_deer)
                curr_deer = 0
            else:
                curr_deer += int(line)
        
        result = sorted(deers, reverse=True)[0]
        return result

def part2():
    curr_deer = 0
    deers = []
    with open('data/day1input.txt') as f:
        for line in f:
            line = line.strip()
            if line == "":
                deers.append(curr_deer)
                curr_deer = 0
            else:
                curr_deer += int(line)
        
        result = sorted(deers, reverse=True)[:3]
        return sum(result)

print(part1())
print(part2())