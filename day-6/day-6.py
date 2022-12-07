import unittest

def is_unique(input):
    return len(input) == len(set(input))

def find_unique(input, length):
    for i, l in enumerate(input):
        if is_unique(input[i:i + length]):
            return i + length

def solve_1(input):
    return find_unique(input, 4)

def solve_2(input):
    return find_unique(input, 14)

with open("./input.txt") as f:
    input = f.read()

example_1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
example_2 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
example_3 = "nppdvjthqldpwncqszvftbrmjlhg"
example_4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
example_5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

class Test(unittest.TestCase):
    def test_solve_1(self):
        self.assertEqual(solve_1(input), 1142)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 2803)

    def test_solve_example_1(self):
        self.assertEqual(solve_1(example_1), 7)
        self.assertEqual(solve_1(example_2), 5)
        self.assertEqual(solve_1(example_3), 6)
        self.assertEqual(solve_1(example_4), 10)
        self.assertEqual(solve_1(example_5), 11)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example_1), 19)
        self.assertEqual(solve_2(example_2), 23)
        self.assertEqual(solve_2(example_3), 23)
        self.assertEqual(solve_2(example_4), 29)
        self.assertEqual(solve_2(example_5), 26)

    def is_unique(self):
        self.assertEqual(is_unique("abcd"), True)
        self.assertEqual(is_unique("aaaa"), False)

unittest.main()
