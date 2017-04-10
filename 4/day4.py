#!/usr/bin/env python

import sys
import collections


ALPHA = list("abcdefghijklmnopqrstuvwxyz")
ALPHA_LEN = len(ALPHA)


def valid_checksum(cipher, checksum):
    count = collections.defaultdict(int)

    for letter in cipher:
        if letter != "-":
            count[letter] += 1

    sort_key = lambda x: (x[1] * -1, x[0])
    sorted_count = sorted(count.items(), key=sort_key)
    valid_checksum = ''.join([x[0] for x in sorted_count])[:5]

    return checksum == valid_checksum


def decrypt(cipher, sector_id):
    plaintext = ""
    for letter in cipher:
        if letter == "-":
            plaintext += " "
        else:
            idx = ALPHA.index(letter)
            plaintext += ALPHA[(idx + sector_id) % ALPHA_LEN]

    return plaintext


total = 0
for line in sys.stdin:
    split = line.split('-')
    checksum = split[-1][4:-2]
    sector_id = int(split[-1][:3])
    cipher = '-'.join(split[:-1])

    if valid_checksum(cipher, checksum):
        total += sector_id
        print(str(sector_id) + "\t" + decrypt(cipher, sector_id))

print(total)
