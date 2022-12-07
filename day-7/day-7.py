import unittest

FILESYSTEM_SIZE = 70000000
SMALL_DIR = 100000
UPDATE_SIZE = 30000000

class Dir:

    def __init__(self):
        self.current_dir = ""
        self.directory_sizes = {}
        self.seen_cards = {}

    def change_directory(self, command):
        directory = command[3:]
        if directory == "..":
            self.current_dir = self.current_dir[:self.current_dir.rindex('/')]
        elif directory == "/":
            self.current_dir = ""
        else:
            self.current_dir += "/" + directory

    def list_directory(self, command):
        for file in command.split('\n')[1:]:
            if file[0:3] != "dir":
                size = int(file.split(" ")[0])
                path = self.current_dir.split("/")
                for i in range(len(path)):
                    dir = "/".join(path[:i+1]) or "/"
                    self.directory_sizes[dir] = self.directory_sizes.get(dir, 0) + size

    available_commands = {
        "cd": change_directory,
        "ls": list_directory,
    }

    def parse_commands(self, input):
        return input.split("$")

    def calculate_big_dirs_sum(self):
        return sum([size for size in self.directory_sizes.values() if size <= SMALL_DIR])

    def find_smallest_big_dir(self):
        minimum_size = UPDATE_SIZE - (FILESYSTEM_SIZE - self.directory_sizes["/"])
        small_dirs = [(dir,size) for dir, size in self.directory_sizes.items() if size >= minimum_size]
        small_dirs_sorted = sorted(small_dirs, key=lambda dir: dir[1])
        return small_dirs_sorted[0][1]

    def calculate_directory_sizes(self, input):
        commands = [command.strip() for command in self.parse_commands(input) if command]
        for command_output in commands:
            command = self.available_commands[command_output[0:2]]
            command(self, command_output)

    def solve_1(self, input):
        self.calculate_directory_sizes(input)
        return self.calculate_big_dirs_sum()

    def solve_2(self, input):
        self.calculate_directory_sizes(input)
        return self.find_smallest_big_dir()

with open("./input.txt") as f:
    input = f.read().strip()

example = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''

class Test(unittest.TestCase):
    def test_solve_1(self):
        dir = Dir()
        self.assertEqual(dir.solve_1(input), 1367870)

    def test_solve_2(self):
        dir = Dir()
        self.assertEqual(dir.solve_2(input), 549173)

    def test_solve_example_1(self):
        dir = Dir()
        self.assertEqual(dir.solve_1(example), 95437)

    def test_solve_example_2(self):
        dir = Dir()
        self.assertEqual(dir.solve_2(example), 24933642)

unittest.main()
