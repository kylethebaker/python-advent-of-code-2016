#!/usr/bin/env python

import sys

easypad = {
    (1, 1): '1', (1, 2): '2', (1, 3): '3',
    (2, 1): '4', (2, 2): '5', (2, 3): '6',
    (3, 1): '7', (3, 2): '8', (3, 3): '9',
}

hardpad = {
                              (1, 3): '1',
                 (2, 2): '2', (2, 3): '3', (2, 4): '4',
    (3, 1): '5', (3, 2): '6', (3, 3): '7', (3, 4): '8', (3, 5): '9',
                 (4, 2): 'A', (4, 3): 'B', (4, 4): 'C',
                              (5, 3): 'D',
}

next_digit = {
    'U': lambda y, x: (y - 1, x),
    'D': lambda y, x: (y + 1, x),
    'L': lambda y, x: (y, x - 1),
    'R': lambda y, x: (y, x + 1),
}

# part 1
#keypad = easypad
#current = (1, 1)

# part 2
keypad = hardpad
current = (3, 1)

code = []

for line in sys.stdin:
    for direction in line.strip():
        possibility = next_digit[direction](*current)
        if possibility in keypad:
            current = possibility
    code.append(keypad[current])

print(code)
