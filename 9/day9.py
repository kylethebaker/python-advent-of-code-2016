#!/usr/bin/env python

import sys
import re


def get_sequences(c):
    seqs = {}
    for m in re.finditer(r"\(\d+x\d+\)", c):
        seq_len, repeat_cnt = m.group()[1:-1].split("x")
        seqs[m.start()] = (m.end(), int(seq_len), int(repeat_cnt))
    return seqs


c = sys.stdin.readline().strip()
seqs = get_sequences(c)
uncompressed = ""

i = 0
while i < len(c):

    if i in seqs:
        seq_start, seq_len, repeat_cnt = seqs[i]
        uncompressed += c[seq_start:seq_start + seq_len] * repeat_cnt
        i = seq_start + seq_len
        continue

    uncompressed += c[i]
    i += 1

print(len(uncompressed))
