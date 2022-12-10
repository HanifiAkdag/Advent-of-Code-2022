def part1():
    head = [0,0]
    tail = [0,0]
    previous_locations = {(0,0)}
    with open('data/day9input.txt') as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            step = int(line[2:])

            for _ in range(step):
                previous = head[:]
                match direction:
                    case 'L':
                        head[0] -= 1
                    case 'R':
                        head[0] += 1
                    case 'D':
                        head[1] -= 1
                    case 'U':
                        head[1] += 1
            
                if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                    tail = previous[:]
                    previous_locations.add(tuple(tail))

    return len(previous_locations)

def part2():
    knots = [[0,0] for _ in range(10)]
    previous_locations = {(0,0)}
    with open('data/day9input.txt') as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            step = int(line[2:])
            for _ in range(step):
                match direction:
                    case 'L':
                        knots[0][0] -= 1
                    case 'R':
                        knots[0][0] += 1
                    case 'D':
                        knots[0][1] -= 1
                    case 'U':
                        knots[0][1] += 1
                for i in range(1, len(knots)):
                    # COPIED FROM SOMEONE ELSE'S SOLUTION
                    row_d = knots[i-1][0] - knots[i][0]
                    col_d = knots[i-1][1] - knots[i][1]

                    if row_d != 0:
                        row_d -= 1 if row_d > 0 else -1

                    if col_d != 0:
                        col_d -= 1 if col_d > 0 else -1

                    if row_d or col_d:
                        knots[i] = (knots[i-1][0] - row_d, knots[i-1][1] - col_d)

                    if i == 9:
                        previous_locations.add(tuple(knots[i]))
    
    

    return (len(previous_locations))

def is_broken(knot1, knot2) -> bool:
    return abs(knot1[0] - knot2[0]) > 1 or abs(knot1[1] - knot2[1]) > 1
print(part2())