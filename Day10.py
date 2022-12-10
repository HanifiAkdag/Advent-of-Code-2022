def part1():
    with open('data/day10input.txt') as f:
        result = 0
        cycle = 1
        register = 1
        for line in f:
            line = line.strip()
            instruction = line[:4]
            if instruction == 'noop':
                cycle += 1
            else:
                value = int(line[5:])
                cycle += 1
                if cycle % 40 == 20:
                    result += cycle * register
                cycle += 1
                register += value
            if cycle % 40 == 20:
                result += cycle * register
        return result

def part2():
    with open('data/day10input.txt') as f:
        cycle = 0
        sprite_pos = 0
        row = ''
        for line in f:
            line = line.strip()
            instruction = line[:4]
            if instruction == 'noop':
                row = draw(cycle, sprite_pos, row)
                cycle += 1
            else:
                value = int(line[5:])
                row = draw(cycle, sprite_pos, row)
                cycle += 1
                if cycle % 40 == 0:
                    print(row)
                    row = ''
                row = draw(cycle, sprite_pos, row)
                cycle += 1
                sprite_pos += value
            if cycle % 40 == 0:
                print(row)
                row = ''

def draw(cycle, sprite_pos, row):
    if (cycle % 40) - sprite_pos < 3 and (cycle % 40) - sprite_pos >= 0:
        row += '#'
    else:
        row += '.'
    return row

print(part1())
part2()
