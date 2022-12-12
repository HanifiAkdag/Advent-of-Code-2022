from queue import PriorityQueue

def heuristic(n, end):
    return abs(end[0] - n[0]) + abs(end[1] - n[1]) + abs(end[2] - n[2])

def get_neighbors(n, grid):
    neighbors = []
    if n[0] > 0:
        neighbors.append(grid[n[1]][n[0] - 1])
    if n[0] < len(grid[0]) - 1:
        neighbors.append(grid[n[1]][n[0] + 1])
    if n[1] > 0:
        neighbors.append(grid[n[1] - 1][n[0]])
    if n[1] < len(grid) - 1:
        neighbors.append(grid[n[1] + 1][n[0]])
    return neighbors

def part1():
    grid = []
    with open('data/day12input.txt') as f:
        for line in f:
            line = line.strip()
            row = []
            for ch in line:
                if ch.islower():
                    z = ord(ch) - ord('a')
                    node = (len(row), len(grid), z)
                    row.append(node)
                elif ch == 'S':
                    start = (len(row), len(grid), 0)
                    row.append(start)
                else:
                    end = (len(row), len(grid), 25)
                    row.append(end)
                
            grid.append(row)

    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = heuristic(start, end)

    while not open_set.empty():
        current = open_set.get()[1]
        if current == end:
            path = []
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return len(path)

        for neighbor in get_neighbors(current, grid):
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor] and neighbor[2] - current[2] <= 1:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic(neighbor, end)
                open_set.put((f_score[neighbor], neighbor))

def part2():
    grid = []
    with open('data/day12input.txt') as f:
        for line in f:
            line = line.strip()
            row = []
            for ch in line:
                if ch == 'E':
                    top = (len(row), len(grid), 25)
                    row.append(top)
                else:
                    z = ord(ch) - ord('a')
                    node = (len(row), len(grid), z)
                    row.append(node)
                
            grid.append(row)
    visited = [top]
    q = [top]
    parents = {top:top}
    while q:
        v = q.pop(0)
        if v[2] == 0:
            result = v
            break
        for neighbor in get_neighbors(v, grid):
            if neighbor not in visited and v[2] - neighbor[2] <= 1:
                visited.append(neighbor)
                parents[neighbor] = v
                q.append(neighbor)


    path = []
    while parents[result] != result:
        path.append(result)
        result = parents[result]
    return len(path)

print(part1())
print(part2())