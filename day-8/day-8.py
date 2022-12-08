import unittest

def north_trees(x, y, trees): return [tree_line[x] for tree_line in trees[:y]]
def west_trees(x, line): return line[:x]
def east_trees(x, line): return line[x + 1:]
def south_trees(x, y, trees): return [tree_line[x] for tree_line in trees[y + 1:]]

def is_visible(tree, candidates):
    return not any([candidate >= tree for candidate in candidates])

def scenic_score(tree, trees):
    score = 0
    for t in trees:
        score += 1
        if t >= tree:
            return score
    return score

def solve_1(input):
    trees = [[int(t) for t in list(line)] for line in input.splitlines()]
    visible = 0
    for y, line in enumerate(trees):
        for x, tree in enumerate(line):
            north = is_visible(tree, north_trees(x, y, trees))
            west = is_visible(tree, west_trees(x, line))
            east = is_visible(tree, east_trees(x, line))
            south = is_visible(tree, south_trees(x, y, trees))
            visible += 1 if west or east or north or south else 0
    return visible

def solve_2(input):
    trees = [[int(t) for t in list(line)] for line in input.splitlines()]
    score = 0
    for y, line in enumerate(trees):
        for x, tree in enumerate(line):
            north = scenic_score(tree, list(reversed(north_trees(x, y, trees))))
            west = scenic_score(tree, list(reversed(west_trees(x, line))))
            east = scenic_score(tree, east_trees(x, line))
            south = scenic_score(tree, south_trees(x, y, trees))
            score = max(score, west * east * north * south)
    return score

with open("./input.txt") as f:
    input = f.read()

example = '''30373
25512
65332
33549
35390
'''

class Test(unittest.TestCase):
    def test_solve_1(self):
        self.assertEqual(solve_1(input), 1736)

    def test_solve_2(self):
        self.assertEqual(solve_2(input), 268800)

    def test_solve_example_1(self):
        self.assertEqual(solve_1(example), 21)

    def test_solve_example_2(self):
        self.assertEqual(solve_2(example), 8)

unittest.main()
