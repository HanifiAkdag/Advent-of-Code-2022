def part1():
    count = 0

    with open('data/day4input.txt') as f:
        for line in f:
            first, second = line.split(',')
            first_start, first_end = map(int, first.split('-'))
            second_start, second_end = map(int, second.split('-'))


            if (first_start <= second_start and first_end >= second_end) or (first_start >= second_start and first_end <= second_end):
                count += 1

        return count

def part2():
    count = 0

    with open('data/day4input.txt') as f:
        for line in f:
            first, second = line.split(',')
            first_start, first_end = map(int, first.split('-'))
            second_start, second_end = map(int, second.split('-'))

            if not (first_end < second_start or second_end < first_start):
                count += 1

        return count

print(part1())
print(part2())