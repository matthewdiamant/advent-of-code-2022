import unittest

def solve_1(input):
    return input

def solve_2(input):
    return input

with open("./input.txt") as f:
    input = f.read()

with open("./example.txt") as f:
    example = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), None)

    def test_solve_1(self):
        return
        self.assertEqual(solve_1(input), None)

    def test_solve_example_2(self):
        return
        self.assertEqual(solve_2(example), None)

    def test_solve_2(self):
        return
        self.assertEqual(solve_2(input), None)

unittest.main()
