import json
from functools import cmp_to_key

def part1():
    with open('data/day13input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        total = 0
        for i in range(len(lines) // 3 + 1):
            first = json.loads(lines[i*3])
            second = json.loads(lines[i*3 + 1])
            result = compare(first, second)
            if result == 1:
                total += i + 1
        return total

def part2():
    with open('data/day13input.txt') as f:
        packets = [[[2]], [[6]]]
        for line in f:
            line = line.strip()
            if line:
                packets.append(json.loads(line))
        packets.sort(key=cmp_to_key(compare), reverse=True)
        return((packets.index([[2]])+1) * (packets.index([[6]])+1))

def compare(original_first, original_second):
    # Both are integer
    if type(original_first) == int and type(original_second) == int:
        return original_second - original_first

    # Both are lists
    elif type(original_first) == list and type(original_second) == list:
        first = original_first.copy()
        second = original_second.copy()
        if not first and not second:
            return 0
        if not first:
            return 1 
        for _ in range(len(first)):
            if not second:
                return -1 
            f = first.pop(0)
            s = second.pop(0)
            result = compare(f, s)
            if result < 0:
                return -1
            elif result > 0:
                return 1
            else:
                continue
        
                
    # One of them is integer
    else:
        if type(original_first) == int:
            second = original_second.copy()
            return compare([original_first], second)
        else:
            first = original_first.copy()
            return compare(first, [original_second])

    return 1

print(part1())
print(part2())