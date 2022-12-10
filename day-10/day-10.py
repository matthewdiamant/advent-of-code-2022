import unittest

def check_cycle(cycle, x, strengths):
  cycle += 1
  if (cycle - 20) % 40 == 0:
    strengths += x * cycle
  return cycle, strengths

def add_pixel_to_screen(cycle, x, screen):
  if x - 1 <= ((cycle - 1) % 40) <= x + 1:
    screen[(cycle - 1) // 40][(cycle - 1) % 40] = "#"
  cycle += 1
  return cycle, screen

def print_screen(screen):
  print()
  for row in screen:
    print("".join(row))

def solve_1(input):
  instructions = [line.split(" ") for line in input.splitlines()]
  x = 1
  cycle = 0
  strengths = 0
  for instruction in instructions:
    if (instruction[0] == "noop"):
      cycle, strengths = check_cycle(cycle, x, strengths)
    elif (instruction[0] == "addx"):
      cycle, strengths = check_cycle(cycle, x, strengths)
      cycle, strengths = check_cycle(cycle, x, strengths)
      x += int(instruction[1])
  return strengths

def solve_2(input):
  instructions = [line.split(" ") for line in input.splitlines()]
  x = 1
  cycle = 1
  screen = [["." for _ in range(40)] for _ in range(6)]

  for instruction in instructions:
    if (instruction[0] == "noop"):
      cycle, screen = add_pixel_to_screen(cycle, x, screen)
    elif (instruction[0] == "addx"):
      cycle, screen = add_pixel_to_screen(cycle, x, screen)
      cycle, screen = add_pixel_to_screen(cycle, x, screen)
      x += int(instruction[1])
  print_screen(screen)

with open("./input.txt") as f:
  input = f.read()

with open("./example.txt") as f:
  example = f.read()

class Test(unittest.TestCase):
  def test_solve_example_1(self):
    self.assertEqual(solve_1(example), 13140)

  def test_solve_1(self):
    self.assertEqual(solve_1(input), 17180)

  def test_solve_example_2(self):
    self.assertEqual(solve_2(example), None)

  def test_solve_2(self):
    self.assertEqual(solve_2(input), None)

unittest.main()