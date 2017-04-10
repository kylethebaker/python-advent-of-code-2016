#!/usr/bin/env python

import sys


def get_ip_pieces(ip):
    body, hypernet = [[]], []
    inside_hyper = False

    for letter in ip:

        if letter == "[":
            inside_hyper = True
            hypernet.append([])
            continue

        if letter == "]":
            inside_hyper = False
            body.append([])
            continue

        if inside_hyper:
            hypernet[-1].append(letter)
        else:
            body[-1].append(letter)

    return ["".join(s) for s in body], ["".join(s) for s in hypernet]


def has_abba(s):
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1]:
            return True
    return False


def get_abas(s):
    abas = []
    for i in range(len(s) - 2):
        if s[i] == s[i + 2] and s[i] != s[i + 1]:
            abas.append(s[i:i + 3])
    return abas


def invert_aba(aba):
    return aba[1] + aba[0] + aba[1]


tls_count, ssl_count = 0, 0
for line in sys.stdin:
    body, hypernet = get_ip_pieces(line.strip())

    body_has_abba = any([has_abba(s) for s in body])
    hypernet_has_abba = any([has_abba(s) for s in hypernet])

    if body_has_abba and not hypernet_has_abba:
        tls_count += 1

    body_abas = []
    for segment in body:
        body_abas.extend(get_abas(segment))

    hypernet_abas = []
    for segment in hypernet:
        hypernet_abas.extend(get_abas(segment))

    has_ssl = False
    for body_aba in body_abas:
        for hypernet_aba in hypernet_abas:
            if hypernet_aba == invert_aba(body_aba):
                has_ssl = True

    if has_ssl:
        ssl_count += 1

print(tls_count)
print(ssl_count)
