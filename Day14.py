def update_rocks(rock_locations: set, inst):
    edges = [tuple(map(int, x.split(','))) for x in inst.split(' -> ')]
    for i in range(len(edges) - 1):
        start = edges[i]
        end = edges[i+1]
        if start[1] > end[1]:   # Going Down
            for y in range(end[1], start[1] + 1):
                rock_locations.add((start[0], y))
        
        elif start[1] < end[1]:
            for y in range(start[1], end[1] + 1):
                rock_locations.add((start[0], y))

        elif start[0] > end[0]:
            for x in range(end[0], start[0] + 1):
                rock_locations.add((x, start[1]))
        
        else:
            for x in range(start[0], end[0] + 1):
                rock_locations.add((x, start[1]))


def part1():
    def pour_sand(rock_locations: set, sand_locations: set, sand: tuple, deepest: int):
        if sand[1] > deepest:
            return None
        while (sand[0], sand[1]+1) not in rock_locations | sand_locations and sand[1] != deepest:
            sand = (sand[0], sand[1]+1)
        if (sand[0]-1, sand[1]+1) not in rock_locations | sand_locations:
            sand = sand[0]-1, sand[1]+1
            return pour_sand(rock_locations, sand_locations, sand, deepest)
        elif (sand[0]+1, sand[1]+1) not in rock_locations | sand_locations:
            sand = sand[0]+1, sand[1]+1
            return pour_sand(rock_locations, sand_locations, sand, deepest)
        else:
            sand_locations.add(sand)
            return sand

    POURING_POINT = (500, 0)
    rock_locations = set()
    with open('data/day14input.txt') as f:
        for inst in f:
            update_rocks(rock_locations, inst.strip())
    sand_locations = set()
    deepest = max(rock_locations, key = lambda t: t[1])[1]
    sand = pour_sand(rock_locations, sand_locations, POURING_POINT, deepest)
    while sand:
        sand = pour_sand(rock_locations, sand_locations, POURING_POINT, deepest)
    
    return len(sand_locations)


def part2():
    def pour_sand(rock_locations: set, sand_locations: set, sand: tuple, rock_bottom: int):
        while (sand[0], sand[1]+1) not in rock_locations | sand_locations and sand[1]+1 != rock_bottom:
            sand = (sand[0], sand[1]+1)
        if (sand[0]-1, sand[1]+1) not in rock_locations | sand_locations and sand[1]+1 != rock_bottom:
            sand = sand[0]-1, sand[1]+1
            return pour_sand(rock_locations, sand_locations, sand, rock_bottom)
        elif (sand[0]+1, sand[1]+1) not in rock_locations | sand_locations and sand[1]+1 != rock_bottom:
            sand = sand[0]+1, sand[1]+1
            return pour_sand(rock_locations, sand_locations, sand, rock_bottom)
        else:
            sand_locations.add(sand)
            return sand
    
    POURING_POINT = (500, 0)
    rock_locations = set()
    with open('data/day14input.txt') as f:
        for inst in f:
            update_rocks(rock_locations, inst.strip())
    sand_locations = set()
    rock_bottom = max(rock_locations, key = lambda t: t[1])[1] + 2
    sand = pour_sand(rock_locations, sand_locations, POURING_POINT, rock_bottom)
    while sand != POURING_POINT:
        print(sand)
        sand = pour_sand(rock_locations, sand_locations, POURING_POINT, rock_bottom)
    
    return len(sand_locations)


print(part1())
print(part2())