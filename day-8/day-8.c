#include <stdio.h>
#include <stdbool.h>

const int SIZE = 99;

struct VisibilityAndScore {
  bool visible;
  int score;
};

struct VisibilityAndScore west(int trees[SIZE][SIZE], int x, int y) {
  int tree = trees[y][x];
  bool visible = true;
  int score = 0;
  for (int i = 0; i < x; i++) {
    if (trees[y][i] >= tree) {
      visible = false;
      break;
    }
  }
  for (int i = x - 1; i >= 0 && !(trees[y][i] >= tree); i--) {
    score += 1;
  }
  return (struct VisibilityAndScore){visible, score};
}

struct VisibilityAndScore east(int trees[SIZE][SIZE], int x, int y) {
  int tree = trees[y][x];
  bool visible = true;
  int score = 0;
  for (int i = x + 1; i < SIZE; i++) {
    score += 1;
    if (trees[y][i] >= tree) {
      visible = false;
      break;
    }
  }
  return (struct VisibilityAndScore){visible, score};
}

struct VisibilityAndScore north(int trees[SIZE][SIZE], int x, int y) {
  int tree = trees[y][x];
  bool visible = true;
  int score = 0;
  for (int i = 0; i < y; i++) {
    if (trees[i][x] >= tree) {
      visible = false;
      break;
    }
  }
  for (int i = y - 1; i >= 0 && !(trees[i][x] >= tree); i--) {
    score += 1;
  }
  return (struct VisibilityAndScore){visible, score};
}

struct VisibilityAndScore south(int trees[SIZE][SIZE], int x, int y) {
  int tree = trees[y][x];
  bool visible = true;
  int score = 0;
  for (int i = y + 1; i < SIZE; i++) {
    score += 1;
    if (trees[i][x] >= tree) {
      visible = false;
      break;
    }
  }
  return (struct VisibilityAndScore){visible, score};
}

int main() {
  FILE *fp;
  fp = fopen("./input.txt", "r");

  int read;
  char *line = NULL;
  size_t len = 0;
  int y = 0;
  int trees[SIZE][SIZE];
  while ((read = getline(&line, &len, fp)) != -1) {
    for (int i = 0; line[i] != '\n'; i++) {
      trees[y][i] = line[i] - '0';
    }
    y += 1;
  }

  int total_visible = 0;
  int best_score = 0;
  for (int y = 0; y < SIZE; y++) {
    for (int x = 0; x < SIZE; x++) {
      int *line = trees[y];
      int tree = line[x];

      struct VisibilityAndScore west_output = west(trees, x, y);
      bool visible = west_output.visible;
      int score = west_output.score;

      struct VisibilityAndScore east_output = east(trees, x, y);
      visible = visible || east_output.visible;
      score *= east_output.score;

      struct VisibilityAndScore north_output = north(trees, x, y);
      visible = visible || north_output.visible;
      score *= north_output.score;

      struct VisibilityAndScore south_output = south(trees, x, y);
      visible = visible || south_output.visible;
      score *= south_output.score;

      if (visible) {
        total_visible += 1;
      }
      if (score > best_score) {
        best_score = score;
      }
    }
  }

  printf("visible: %d\n", total_visible);
  printf("best scenic score: %d\n", best_score);

  return 0;
}