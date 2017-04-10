#!/usr/bin/env python

import sys
from collections import defaultdict


class Grid(object):

    def __init__(self):
        self.position = {'x': 0, 'y': 0}
        self.destination = {'x': 0, 'y': 0}
        self.visited = defaultdict(int)
        self.facing = 0
        self.first_visited_twice = None

    def find_destination(self, directions):
        for direction, steps in directions:
            self.turn(direction)
            self.move(steps)
        self.destination = self.position.copy()
        self.reset_position()

    def turn(self, direction):
        if direction == 'R':
            self.facing += 90
        elif direction == 'L':
            self.facing -= 90

        self.facing %= 360

    def move(self, steps):
        for i in range(steps):
            if self.facing == 0:
                self.position['y'] += 1
            elif self.facing == 90:
                self.position['x'] += 1
            elif self.facing == 180:
                self.position['y'] -= 1
            elif self.facing == 270:
                self.position['x'] -= 1

            current = (self.position['x'], self.position['y'])
            self.visited[current] += 1

            if self.first_visited_twice is None and self.visited[current] == 2:
                self.first_visited_twice = current

    def reset_position(self):
        self.position = {'x': 0, 'y': 0}
        self.facing = 0

    def get_distance_from_dest(self):
        return abs(self.destination['x']) + abs(self.destination['y'])

    def get_distance_from_first_visited_twice(self):
        x, y = self.first_visited_twice
        return abs(x) + abs(y)


directions = [x.strip() for x in sys.stdin.readline().split(',')]
directions = [(i[0], int(i[1:])) for i in directions]

grid = Grid()
grid.find_destination(directions)
print(grid.get_distance_from_dest())
print(grid.get_distance_from_first_visited_twice())
