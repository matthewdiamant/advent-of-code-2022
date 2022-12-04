import unittest

def is_full_crossover(pair):
    a, b = pair[0].split("-")
    x, y = pair[1].split("-")
    a = int(a); b = int(b); x = int(x); y = int(y)
    return (a >= x and b <= y) or (x >= a and y <= b)

def is_crossover(pair):
    a, b = pair[0].split("-")
    x, y = pair[1].split("-")
    a = int(a); b = int(b); x = int(x); y = int(y)
    return (x <= a <= y) or (a <= x <= b)

def sum_crossovers(input, crossover_decider):
    return sum([crossover_decider(pair.split(",")) for pair in input])

def solve_1(input):
    return sum_crossovers(input, is_full_crossover)

def solve_2(input):
    return sum_crossovers(input, is_crossover)

with open("./input.txt") as f:
    input = f.read().splitlines()

class Test(unittest.TestCase):
    def test_solve_1(self):
        self.assertEqual(solve_1(input), 450)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 837)

unittest.main()
