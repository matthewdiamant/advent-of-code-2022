from math import inf
import unittest

BUFFER = 110

def drip(grid):
    sand = [500, 0]
    while True:
        x, y = [sand[0], sand[1] + 1]
        if grid[y][x] == ".":
            sand = [x, y]; continue
        x, y = [sand[0] - 1, sand[1] + 1]
        if grid[y][x] == ".":
            sand = [x, y]; continue
        x, y = [sand[0] + 1, sand[1] + 1]
        if grid[y][x] == ".":
            sand = [x, y]; continue
        break
    grid[sand[1]][sand[0]] = "o"
    return grid, sand

def count_drips_until_test(grid, max_y, test):
    result = 0
    while True:
        grid, last_drip = drip(grid)
        if test(last_drip, max_y):
            return result
        result += 1

def test_1(last_sand, max_y):
    return last_sand[1] > max_y - 1

def test_2(last_sand, _):
    return last_sand[0] == 500 and last_sand[1] == 0

def create_grid(input):
    paths = [
        [
            [int(coord) for coord in node.split(",")]
        for node in path.split(" -> ")]
    for path in input.splitlines()]
    
    min_x = inf; max_x = 0; max_y = 0
    for path in paths:
        for x, y in path:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

    grid = [["." for _ in range(max_x + 1 + BUFFER)] for _ in range(max_y + 2)]
    grid.append(["#" for _ in range(max_x + 1 + BUFFER)]) 

    for path in paths:
        for i, _ in enumerate(path):
            if i == len(path) - 1: continue
            start_x, start_y = path[i]
            end_x, end_y = path[i + 1]
            end_x += 1 if start_x <= end_x else -1
            end_y += 1 if start_y <= end_y else -1
            for x in range(start_x, end_x, 1 if start_x <= end_x else -1):
                for y in range(start_y, end_y, 1 if start_y <= end_y else -1):
                    grid[y][x] = "#"

    return grid, max_y

def solve_1(input):
    grid, max_y = create_grid(input)
    return count_drips_until_test(grid, max_y, test_1)

def solve_2(input):
    grid, max_y = create_grid(input)
    return count_drips_until_test(grid, max_y, test_2) + 1

with open("./input.txt") as f:
    input = f.read()

with open("./example.txt") as f:
    example = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 24)

    def test_solve_1(self):
        return
        self.assertEqual(solve_1(input), 625)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example), 93)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 25193)

unittest.main()
