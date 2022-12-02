import unittest

def split_lines(input):
    return list(filter(None, input.split("\n")))

def sum_list(list):
    return sum([int(n) for n in list])

def sorted_sums(input):
    groups = input.split("\n\n")
    sums = [sum_list(split_lines(group)) for group in groups]
    return sorted(sums, reverse=True)

def solve_1(input):
    return sorted_sums(input)[0]

def solve_2(input):
    return sum(sorted_sums(input)[:3])

with open("./input.txt") as f:
    input = f.read()
    solve_1(input)
    solve_2(input)

class Test(unittest.TestCase):
    def test_solve_1(self):
        self.assertEqual(solve_1(input), 70764)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 203905)

unittest.main()
