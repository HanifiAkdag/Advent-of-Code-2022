from collections import defaultdict
import re

def part1():
    d = defaultdict(list)

    with open('data/day5input.txt') as f:
        lines = f.readlines()
        curr = 0
        pattern = r'\[(\w)\]'
        while not lines[curr].startswith(' 1'):
            for match in re.finditer(pattern, lines[curr]):
                stack_code = match.span()[0] // 4
                d[stack_code].append(match[1])
            curr += 1
        stacks = list(map(lambda x: list(reversed(x)),  dict(sorted(d.items())).values()))

        curr += 2

        for i in range(curr, len(lines)):
            pattern = r'[0-9]+'
            amount, source, dest = map(int, re.findall(pattern, lines[i]))
            for _ in range(amount):
                tmp = stacks[source - 1].pop()
                stacks[dest - 1].append(tmp)

        result = ''.join([stack[-1] for stack in stacks])
        return result

def part2():
    d = defaultdict(list)

    with open('data/day5input.txt') as f:
        lines = f.readlines()
        curr = 0
        pattern = r'\[(\w)\]'
        while not lines[curr].startswith(' 1'):
            for match in re.finditer(pattern, lines[curr]):
                stack_code = match.span()[0] // 4
                d[stack_code].append(match[1])
            curr += 1
        stacks = list(map(lambda x: list(reversed(x)),  dict(sorted(d.items())).values()))
    
    curr += 2

    for i in range(curr, len(lines)):
        pattern = r'[0-9]+'
        amount, source, dest = map(int, re.findall(pattern, lines[i]))
        stacks[dest - 1].extend(stacks[source - 1][-amount:])
        stacks[source - 1] = stacks[source - 1][:len(stacks[source - 1]) - amount]

    result = ''.join([stack[-1] for stack in stacks])
    return result
    
print(part1())
print(part2())
