#!/usr/bin/env python

import sys
from collections import Counter


def most_common(code):
    msg = ""
    for chars in code:
        msg += Counter(chars).most_common(1)[0][0]
    return msg


def least_common(code):
    msg = ""
    for chars in code:
        msg += Counter(chars).most_common()[-1][0]
    return msg


code = [[] for _ in range(8)]
plaintext = [None] * 8


for line in sys.stdin:
    for col, char in enumerate(line.strip()):
        code[col].append(char)

print("".join(most_common(code)))
print("".join(least_common(code)))
