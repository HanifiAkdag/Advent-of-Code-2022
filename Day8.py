import numpy as np

def part1():
    with open('data/day8input.txt') as f:
        matrix = []
        for line in f:
            row = []
            line = line.strip()
            for char in line:
                row.append(int(char))
            matrix.append(row)
        matrix = np.array(matrix)

    visible = len(matrix)*2 + len(matrix[0])*2 - 4
    for i, row in enumerate(matrix[1:-1], 1):
        for j, num in enumerate(row[1:-1], 1):
            column = matrix[:,j]
            if all(num > column[:i]) or all(num > column[i+1:]) or all(num > row[:j]) or all(num > row[j+1:]):
                visible += 1

    return visible

def part2():
    with open('data/day8input.txt') as f:
        matrix = []
        for line in f:
            row = []
            line = line.strip()
            for char in line:
                row.append(int(char))
            matrix.append(row)
        matrix = np.array(matrix)

    biggest_score = 0
    for i, row in enumerate(matrix[1:-1], 1):
        for j, num in enumerate(row[1:-1], 1):
            column = matrix[:,j]
            score, left, right, top, down = 0, 0, 0, 0, 0
            dist = 1
            while j - dist >= 1:
                if num > row[j - dist]:
                    dist += 1
                else:
                    break
            left = dist
            dist = 1

            while j + dist < len(matrix[0]) - 1:
                if num > row[j + dist]:
                    dist += 1
                else:
                    break
            right = dist
            dist = 1

            while i - dist >= 1:
                if num > column[i - dist]:
                    dist += 1
                else:
                    break
            top = dist
            dist = 1

            while i + dist < len(matrix) - 1:
                if num > column[i + dist]:
                    dist += 1
                else:
                    break
            down = dist
            dist = 1

            score = left*right*top*down
            if score > biggest_score:
                biggest_score = score
        
    return biggest_score

print(part1())
print(part2())