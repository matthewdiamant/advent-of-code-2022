import unittest

def is_ordered(left, right):
    for i in range(len(left)):
        if i >= len(right):
            return False
        if isinstance(left[i], list) and isinstance(right[i], list):
            if left[i] == right[i]:
                continue
            return is_ordered(left[i], right[i])
        if isinstance(left[i], int) and isinstance(right[i], list):
            if [left[i]] == right[i]:
                continue
            return is_ordered([left[i]], right[i])
        if isinstance(left[i], list) and isinstance(right[i], int):
            if left[i] == [right[i]]:
                continue
            return is_ordered(left[i], [right[i]])
        if left[i] == right[i]:
            continue
        return left[i] < right[i]
    return True

def solve_1(input):
    pairs = [[eval(p) for p in pair.split("\n")] for pair in input.split("\n\n")]
    count = 0
    for i, pair in enumerate(pairs):
        if is_ordered(pair[0], pair[1]):
            count += i + 1
    return count

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if not is_ordered(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def solve_2(input):
    signals = [eval(line) for line in input.split("\n") if len(line)]
    signals.append([[2]])
    signals.append([[6]])
    sorted_signals = bubble_sort(signals)
    result = 1
    for i, signal in enumerate(sorted_signals):
        # print(i, signal)
        if signal == [[2]] or signal == [[6]]:
            result *= i + 1
    return result

from functools import cmp_to_key
from math import prod
from ast import literal_eval

mark = [[[2]], [[6]]]

def cmp(l, r):
    match l, r:
        case int(), int(): return l - r
        case list(), int(): r = [r]
        case int(), list(): l = [l]
    return next((c for c in map(cmp, l, r) if c), len(l) - len(r))

with open('./input.txt') as f:
    pkts = list(map(literal_eval, [l for l in f if l.strip()]))

print(sum(i for i, p in enumerate(zip(pkts[::2], pkts[1::2]), 1) if cmp(*p) <= 0))
print(prod(i for i, p in enumerate(sorted(pkts + mark, key=cmp_to_key(cmp)), 1) if p in mark))


with open("./input.txt") as f:
    input = f.read()

with open("./example.txt") as f:
    example = f.read()

class Test(unittest.TestCase):
    def test_solve_example_1(self):
        return
        self.assertEqual(solve_1(example), 13)

    def test_solve_1(self):
        return
        self.assertEqual(solve_1(input), 6046)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example), 140)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 21423)

unittest.main()
