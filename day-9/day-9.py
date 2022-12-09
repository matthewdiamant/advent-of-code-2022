import unittest

def move(leader, follower, dh):
    leader = (leader[0] + dh[0], leader[1] + dh[1])
    dt = (0, 0)
    if (abs(leader[0] - follower[0]) > 1 or abs(leader[1] - follower[1]) > 1):
        if (follower[0] < leader[0]): dt = (1, 0)
        if (follower[0] > leader[0]): dt = (-1, 0)
        if (follower[1] < leader[1]): dt = (dt[0], 1)
        if (follower[1] > leader[1]): dt = (dt[0], -1)
        follower = (follower[0] + dt[0], follower[1] + dt[1])
    return leader, follower

def solve(input, num_knots):
    knots = [(0, 0)] * num_knots
    seen = set()
    DIRS = { "U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0) }
    for instruction in input.splitlines():
        dir, val = instruction.split(" ")
        dh = DIRS[dir]
        for _ in range(int(val)):
            for i in range(len(knots) - 1):
                leader, follower = move(knots[i], knots[i + 1], dh if i == 0 else (0, 0))
                knots[i] = leader
                knots[i + 1] = follower
                if i + 1 == len(knots) - 1:
                    seen.add(knots[i + 1])
    return len(seen)

def solve_1(input):
    return solve(input, 2)

def solve_2(input):
    return solve(input, 10)

with open("./input.txt") as f:
    input = f.read()

example = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
'''

example_2 = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
'''

class Test(unittest.TestCase):
    def test_solve_1(self):
        self.assertEqual(solve_1(input), 5930)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 2443)

    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 13)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example_2), 36)

unittest.main()
