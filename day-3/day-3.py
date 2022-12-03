import unittest

def solve(input):
    return input

with open("./input.txt") as f:
    input = f.read()

class Test(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(input), None)

unittest.main()
