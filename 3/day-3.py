#!/usr/bin/env python

import sys


def is_triangle(t):
    t = sorted(t)
    return t[0] + t[1] > t[2]

in_list = [[int(side) for side in line.split()] for line in sys.stdin]

print("part 1: ", sum(is_triangle(t) for t in in_list))

triangles = []
while in_list:
    square = [in_list.pop() for _ in range(3)]
    for triangle in [[square[y][x] for y in range(3)] for x in range(3)]:
        triangles.append(triangle)

print("part 2: ", sum(is_triangle(t) for t in triangles))
