main = do
  contents <- readFile "input.txt"
  putStr $ solve_part_1 contents

solve_part_1 input = input
