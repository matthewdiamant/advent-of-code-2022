from collections import deque
import unittest

def snafu_to_decimal(snafu_number):
    decimal = 0
    place = 1
    digits = reversed(list(snafu_number))
    for digit in digits:
        if digit  == "=":
            adder = -2
        elif digit  == "-":
            adder = -1
        else:
            adder = int(digit) 
        decimal += int(adder) * place
        place *= 5
    return decimal

def inc_snafu(digit):
    d = {
        "=": ("0", "-"),
        "-": ("0", "0"),
        "0": ("0", "1"),
        "1": ("0", "2"),
        "2": ("1", "="),
    }
    return d[digit]

def digit_to_snafu(digit):
    d = {
        0: ("0", "0"),
        1: ("0", "1"),
        2: ("0", "2"),
        3: ("1", "="),
        4: ("1", "-"),
    }
    return d[digit]

def decimal_to_snafu(decimal):
    snafu = deque(["0"])
    while decimal > 0:
        snafu.appendleft("0")
        n = decimal % 5
        a, b = digit_to_snafu(n)
        if snafu[1] == "0":
            snafu[1] = b
        else:
            x, y = inc_snafu(b)
            snafu[0] = x
            snafu[1] = y
        if snafu[0] == "0":
            snafu[0] = a
        else:
            x, y = inc_snafu(a)
            snafu[0] = y
        decimal -= n
        decimal //= 5
    result = "".join(snafu)
    return result if result[0] != "0" else result[1:]

def solve_1(input):
    snafu_numbers = input.splitlines()
    decimal_numbers = [snafu_to_decimal(snafu_number) for snafu_number in snafu_numbers]
    sum_of_decimals = sum(decimal_numbers)
    return decimal_to_snafu(sum_of_decimals)

with open("./input.txt") as f:
    input = f.read()

with open("./example.txt") as f:
    example = f.read()

class Test(unittest.TestCase):
    def test_snafu_to_decimal_example_1(self):
        self.assertEqual(decimal_to_snafu(3), "1=")

    def test_snafu_to_decimal_example_2(self):
        self.assertEqual(decimal_to_snafu(8), "2=")

    def test_snafu_to_decimal_example_3(self):
        self.assertEqual(decimal_to_snafu(15), "1=0")

    def test_snafu_to_decimal_example_4(self):
        self.assertEqual(decimal_to_snafu(314159265), "1121-1110-1=0")

    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), "2=-1=0")

    def test_solve_1(self):
        self.assertEqual(solve_1(input), "2=01-0-2-0=-0==-1=01")

unittest.main()
