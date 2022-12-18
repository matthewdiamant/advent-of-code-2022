from collections import deque
import unittest

def solve_1(input):
    nodes = [list(i) for i in input.splitlines()]

    for y in range(len(nodes)):
        for x in range(len(nodes[0])):
            if nodes[y][x] == "S":
                start = (y, x)
                nodes[y][x] = "a"
            if nodes[y][x] == "E":
                end = (y, x)
                nodes[y][x] = "z"

    queue = deque([(start[0], start[1], 0)])
    visited = set()

    while queue:
        a, b, c = queue.popleft()
        if (a, b) == end:
            return c
        if (a, b) in visited:
            continue
        visited.add((a, b))
        for i in range(a - 1, a + 2):
            for r in range(b - 1, b + 2):
                if len(nodes) > i >= 0 and len(nodes[0]) > r >= 0 and (i == a or r == b):
                    value = ord(nodes[a][b]) 
                    new_value = ord(nodes[i][r])
                    if new_value <= value + 1:
                        queue.append((i, r, c + 1))

def solve_2(input):
    return input

with open("./input.txt") as f:
    input = f.read()

with open("./example.txt") as f:
    example = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 31)

    def test_solve_1(self):
        self.assertEqual(solve_1(input), 534)

    def test_solve_example_2(self):
        return
        self.assertEqual(solve_2(example), None)

    def test_solve_2(self):
        return
        self.assertEqual(solve_2(input), None)

unittest.main()
