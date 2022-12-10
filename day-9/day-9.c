#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

const int instructions_count = 2000;

struct Coord {
  int x;
  int y;
};

struct Instruction {
  char name;
  int value;
};

struct KnotPair {
  struct Coord leader;
  struct Coord follower;
};

struct KnotPair move(struct Coord leader, struct Coord follower, struct Coord dh) {
  struct Coord new_leader = {leader.x + dh.x, leader.y + dh.y};
  struct Coord new_follower = {follower.x, follower.y};
  struct Coord dt = {0, 0};
  if (abs(new_leader.x - follower.x) > 1 || abs(new_leader.y - follower.y) > 1) {
    if (follower.x < leader.x) dt.x = 1;
    if (follower.x > leader.x) dt.x = -1;
    if (follower.y < leader.y) dt.y = 1;
    if (follower.y > leader.y) dt.y = -1;
    new_follower = (struct Coord) {follower.x + dt.x, follower.y + dt.y};
  }
  return (struct KnotPair) {new_leader, new_follower};
}

int solve(struct Instruction *instructions, int knots_count) {
  struct Coord knots[knots_count];
  for (int i = 0; i < knots_count; i++) {
    knots[i] = (struct Coord) {0, 0};
  }

  struct Coord seen[6000];
  int seen_count = 0;

  for (int i = 0; i < instructions_count; i++) {
    struct Instruction instruction = instructions[i];
    struct Coord dh;
    if (instruction.name == 'U') {
      dh = (struct Coord) {0, 1};
    } else if (instruction.name == 'D') {
      dh = (struct Coord) {0, -1};
    } else if (instruction.name == 'L') {
      dh = (struct Coord) {-1, 0};
    } else if (instruction.name == 'R') {
      dh = (struct Coord) {1, 0};
    }

    for (int n = 0; n < instruction.value; n++) {
      for (int k = 0; k < knots_count - 1; k++) {
        struct KnotPair result = move(knots[k], knots[k + 1], dh);
        knots[k] = result.leader;
        knots[k + 1] = result.follower;

        if (k + 1 == (knots_count - 1)) {
          bool should_add = true;
          for (int s = 0; s < seen_count; s++) {
            if (seen[s].x == knots[k + 1].x && seen[s].y == knots[k + 1].y) {
              should_add = false;
              break;
            }
          }
          if (should_add) {
            seen[seen_count] = knots[k + 1];
            seen_count += 1; 
          }
        }
      }
    }
  }

  return seen_count;
}

int main() {
  FILE *fp;
  fp = fopen("./example.txt", "r");

  int read;
  char *line = NULL;
  size_t len = 0;
  struct Instruction instructions[instructions_count];

  int i = 0;
  while ((read = getline(&line, &len, fp)) != -1) {
    char name = line[0];
    char *v = line + 2;
    int value = atoi(v);
    struct Instruction instruction = {name, value};
    instructions[i] = instruction;
    i += 1;
  }

  int result1 = solve(instructions, 2);
  printf("Result 1: %d\n", result1);
  int result2 = solve(instructions, 10);
  printf("Result 2: %d\n", result2);
}