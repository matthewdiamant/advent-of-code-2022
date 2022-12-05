import re
import unittest

def build_stacks(input):
    num_stacks = int(input.splitlines()[-1].strip()[-1])
    stacks = [[] for i in range(num_stacks)]
    for line in input.splitlines()[:-1]:
        for i in range(0, len(line), 4):
            item = line[i + 1]
            if item != ' ': stacks[i // 4].insert(0, item)
    return stacks

def build_directions(input):
    return [[int(i) for i in re.findall(r'\d+', line)] for line in input.splitlines()]

def tops_of_stacks(stacks):
    return ''.join([stack[-1] for stack in stacks])

def execute_stacks_9000(stacks, directions):
    for num_moves, start, end in directions:
        for i in range(num_moves):
            item = stacks[start - 1].pop()
            stacks[end - 1].append(item)
    return stacks

def execute_stacks_9001(stacks, directions):
    for num_moves, start, end in directions:
        items = stacks[start - 1][-num_moves:]
        stacks[start - 1] = stacks[start - 1][:-num_moves]
        stacks[end - 1] += items
    return stacks

def solve(operation, input):
    stacks_input, directions_input = input.split('\n\n')
    stacks = build_stacks(stacks_input)
    directions = build_directions(directions_input)
    end_stacks = operation(stacks, directions)
    return tops_of_stacks(end_stacks)

def solve_1(input):
    return solve(execute_stacks_9000, input)

def solve_2(input):
    return solve(execute_stacks_9001, input)

with open("./input.txt") as f:
    input = f.read()

example = '''
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

class Test(unittest.TestCase):
    def test_solve_1(self):
        self.assertEqual(solve_1(input), 'WCZTHTMPS')

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 'BLSGJSDTS')

    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 'CMZ')

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example), 'MCD')

unittest.main()
