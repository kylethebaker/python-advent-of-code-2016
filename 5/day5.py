#!/usr/bin/env python

import sys
from itertools import count
from hashlib import md5


def get_hash(door_id, i):
    return md5(door_id + str(i).encode("ascii")).hexdigest()


def decrypt1(door_id):
    password = ""

    for i in count():
        h = get_hash(door_id, i)
        if h[:5] == "0" * 5:
            password += h[5]
        if len(password) == 8:
            break

    return password


def decrypt2(door_id):
    password = [None] * 8

    for i in count():
        h = get_hash(door_id, i)

        if h[:5] == "0" * 5:
            if not str.isdigit(h[5]):
                continue
            pos, digit = int(h[5]), h[6]
            if pos in range(8) and password[pos] is None:
                password[pos] = digit

        if all(password):
            break

    return "".joint(password)

door_id = sys.stdin.readline().strip().encode("ascii")
print(decrypt2(door_id))
