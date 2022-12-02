import unittest

outcome_points = {
  "A": {
    "X": 3,
    "Y": 6,
    "Z": 0,
  },
  "B": {
    "X": 0,
    "Y": 3,
    "Z": 6,
  },
  "C": {
    "X": 6,
    "Y": 0,
    "Z": 3,
  },
}

shape_points = {
  "X": 1,
  "Y": 2,
  "Z": 3,
}

outcomes = {
  "A": {
    "X": "Z",
    "Y": "X",
    "Z": "Y",
  },
  "B": {
    "X": "X",
    "Y": "Y",
    "Z": "Z",
  },
  "C": {
    "X": "Y",
    "Y": "Z",
    "Z": "X",
  },
}

def count_points(shapes):
    return shape_points[shapes[1]] + outcome_points[shapes[0]][shapes[1]]

def determine_outcomes(shapes):
    return [shapes[0], outcomes[shapes[0]][shapes[1]]]

def solve_1(input):
    return sum([count_points(line.split(" ")) for line in input])

def solve_2(input):
    return sum([count_points(determine_outcomes(line.split(" "))) for line in input])

with open("./input.txt") as f:
    input = f.read().splitlines()

class Test(unittest.TestCase):
    def test_solve_1(self):
        self.assertEqual(solve_1(input), 10994)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 12526)

unittest.main()
