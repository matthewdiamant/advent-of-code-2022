import math
import string
import unittest

def priority(item):
    all = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    return all.index(item) + 1

def find_common_1_sack(items):
    half_length = math.floor(len(items) / 2)
    first = items[:half_length]
    second = items[half_length:]
    for letter in first:
        if (letter in second): return letter

def find_common_3_sacks(sacks):
    for letter in sacks[0]:
        if (letter in sacks[1] and letter in sacks[2]): return letter

def solve_1(input):
    return sum([priority(find_common_1_sack(line)) for line in input])

def solve_2(input):
    groups = list(input[i:i+3] for i in range(0, len(input), 3))
    return sum([priority(find_common_3_sacks(n)) for n in groups])

with open("./input.txt") as f:
    input = f.read().splitlines()

class Test(unittest.TestCase):

    def test_find_common_1(self):
        sample = 'vJrwpWtwJgWrhcsFMMfFFhFp'
        self.assertEqual(find_common_1_sack(sample), 'p')

    def test_find_common_2(self):
        sample = 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
        self.assertEqual(find_common_1_sack(sample), 'L')

    def test_find_common_3(self):
        sample = 'PmmdzqPrVvPwwTWBwg'
        self.assertEqual(find_common_1_sack(sample), 'P')

    def test_find_common_4(self):
        sample = 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'
        self.assertEqual(find_common_1_sack(sample), 'v')

    def test_find_common_5(self):
        sample = 'ttgJtRGJQctTZtZT'
        self.assertEqual(find_common_1_sack(sample), 't')

    def test_find_common_6(self):
        sample = 'CrZsJsPPZsGzwwsLwLmpwMDw'
        self.assertEqual(find_common_1_sack(sample), 's')

    def test_solve_1(self):
        self.assertEqual(solve_1(input), 7763)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 2569)

unittest.main()
