import re, time

def manhattan(pos1, pos2):
    return abs(pos1[0] - pos2[0]) +  abs(pos1[1] - pos2[1])

def part1():
    ROW = 2000000
    sensors = dict()
    with open('data/day15input.txt') as f:
        pattern = r'-?\d+'
        for line in f:
            x = re.findall(pattern, line)
            sensors[(int(x[0]), int(x[1]))] = (int(x[2]), int(x[3]))
    
    impossible_points = set()
        
    for sensor, beacon in sensors.items():
        dist = manhattan(sensor, beacon)
        if dist < abs(sensor[1] - ROW):
            continue
        impossible_points.add(sensor[0])
        for i in range(1, dist - abs(sensor[1] - ROW)+1):
            impossible_points.add(sensor[0]+i)
            impossible_points.add(sensor[0]-i)

        if beacon[1] == ROW:
            impossible_points.remove(beacon[0])
        
    return len(impossible_points)

def part2():
    def mergeIntervals(intervals):
        intervals.sort()
        stack = []
        stack.append(intervals[0])
        for i in intervals[1:]:
            if stack[-1][0] <= i[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], i[-1])
            else:
                stack.append(i)
        return stack
    

    MAX_COORD = 4000000
    sensors = dict()
    with open('data/day15input.txt') as f:
        pattern = r'-?\d+'
        for line in f:
            x = re.findall(pattern, line)
            sensors[(int(x[0]), int(x[1]))] = (int(x[2]), int(x[3]))

    # Had to check solutions of others for this part
    for row in range(MAX_COORD+1):
        occupied_spaces = []
        for sensor, beacon in sensors.items():
            distance_to_beacon = manhattan(sensor, beacon)
            distance_to_row = abs(sensor[1] - row)
            if distance_to_row <= distance_to_beacon:
                closest_from_target_y = sensor[0]
                to_go = distance_to_beacon - distance_to_row
                min_x, max_x = (closest_from_target_y - to_go, closest_from_target_y + to_go)
                occupied_spaces.append([max(0, min_x), min(max_x, MAX_COORD)])

        merged_intervals = mergeIntervals(occupied_spaces)
        if merged_intervals[0] != [0, 4000000]:
            print((merged_intervals[0][1] + 1) * MAX_COORD + row)
            break


    
    
part2()