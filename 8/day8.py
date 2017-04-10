#!/usr/bin/env python

import sys
import re


def parse_instruction(ins):
    args = [int(x) for x in re.findall(r"\d+", ins)]
    split = ins.split()
    if split[0] == "rect":
        return toggle_rect, args
    if split[1] == "row":
        return rotate_row, args
    if split[1] == "column":
        return rotate_column, args


def toggle_rect(grid, width, height):
    for y in range(height):
        for x in range(width):
            grid[y][x] = not grid[y][x]


def rotate_row(grid, row, shift):
    num_cols = len(grid[row])
    new_row = list([None] * num_cols)

    for i in range(num_cols):
        new_row[i] = grid[row][i - shift % num_cols]

    grid[row] = new_row


def rotate_column(grid, col, shift):
    num_rows = len(grid)
    new_col = list([None] * num_rows)

    for i in range(num_rows):
        new_col[i] = grid[i - shift % num_rows][col]

    for i in range(num_rows):
        grid[i][col] = new_col[i]


def enabled_lights(grid):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]:
                count += 1
    return count


def draw_grid(grid):
    for row in grid:
        for col in row:
            print("#" if col else ".", end="")
        print()


grid = [x[:] for x in [[False] * 50] * 6]

for line in sys.stdin:
    handler, args = parse_instruction(line.strip())
    handler(grid, *args)

print(enabled_lights(grid))
draw_grid(grid)
