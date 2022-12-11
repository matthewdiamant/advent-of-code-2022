from math import prod
import unittest

class Monkey:
  def __init__(self, lines):
    self.id = lines[0][-2]
    self.items = [int(item) for item in lines[1].split(": ")[1].split(", ")]
    self.operation = lines[2].split(" = ")[1]
    self.test = int(lines[3].split(" ")[-1])
    self.true_case = int(lines[4][-1])
    self.false_case = int(lines[5][-1])
    self.inspect_count = 0
  
  def __repr__(self):
    return f"Monkey {self.id} with {self.items} items, operation {self.operation}, test {self.test}, true case {self.true_case}, false case {self.false_case}, inspect count {self.inspect_count}\n"

def play_round(monkeys, worry, lcm):
  for monkey in monkeys:
    for item in monkey.items:
      monkey.inspect_count += 1
      new = (eval(monkey.operation, {}, {"old": int(item)}) // worry) % lcm
      if new % monkey.test == 0:
        monkeys[monkey.true_case].items.append(new)
      else:
        monkeys[monkey.false_case].items.append(new)
    monkey.items = []

def solve(input, rounds, worry):
  monkeys = [Monkey(monkey.splitlines()) for monkey in input.split("\n\n")]
  lcm = prod([monkey.test for monkey in monkeys])
  for _ in range(rounds):
    play_round(monkeys, worry, lcm)
  counts = [monkey.inspect_count for monkey in sorted(monkeys, key=lambda monkey: monkey.inspect_count, reverse=True)]
  return counts[0] * counts[1]

def solve_1(input):
  return solve(input, 20, 3)

def solve_2(input):
  return solve(input, 10000, 1)

with open("./input.txt") as f:
  input = f.read()

with open("./example.txt") as f:
  example = f.read()

class Test(unittest.TestCase):
  def test_solve_example_1(self):
    self.assertEqual(solve_1(example), 10605)

  def test_solve_1(self):
    self.assertEqual(solve_1(input), 66802)

  def test_solve_example_2(self):
    self.assertEqual(solve_2(example), 2713310158)

  def test_solve_2(self):
    self.assertEqual(solve_2(input), 21800916620)

unittest.main()
