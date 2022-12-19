from collections import defaultdict
from math import inf
import unittest

def create_sensors(input):
    lines = input.splitlines()
    sensors = []
    for line in lines:
        _, b, c, d, e = line.split("=")
        s_x = int(b.split(",")[0])
        s_y = int(c.split(":")[0])
        b_x = int(d.split(",")[0])
        b_y = int(e)
        sensors.append((s_x, s_y, b_x, b_y))
    return sensors

def solve_1(input, row):
    sensors = create_sensors(input)
    grid = defaultdict(list)
    for sensor in sensors:
        s_x, s_y, b_x, b_y = sensor
        distance = abs(s_x - b_x) + abs(s_y - b_y) + 1
        for a in range(distance):
            b = distance - a
            grid[s_y + a].append((s_x - b + 1, s_x + b - 1))
            grid[s_y - a].append((s_x - b + 1, s_x + b - 1))
    result = set()
    for start, end in grid[row]:
        for i in range(start, end + 1):
            result.add(i)
    for s_x, s_y, b_x, b_y in sensors:
        if b_y == row and b_x in result:
            result.remove(b_x)
    return len(result)

def solve_2(input, max_y):
    sensors = create_sensors(input)
    grid = defaultdict(set)
    for sensor in sensors:
        s_x, s_y, b_x, b_y = sensor
        distance = abs(s_x - b_x) + abs(s_y - b_y) + 1
        for a in range(distance):
            b = distance - a
            grid[s_y + a].add((s_x - b + 1, s_x + b - 1))
            grid[s_y - a].add((s_x - b + 1, s_x + b - 1))
    for y in range(max_y):
        if y % 100 == 0:
            print(y)
        row = grid[y]
        a = []
        for start, end in row:
            a = a + list(range(start, end + 1))

with open("./input.txt") as f:
    input = f.read()

with open("./example.txt") as f:
    example = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example, 10), 26)

    def test_solve_1(self):
        return 
        self.assertEqual(solve_1(input, 2000000), None)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example, 20), 56000011)

    def test_solve_2(self):
        self.assertEqual(solve_2(input, 4000000), None)

unittest.main()
