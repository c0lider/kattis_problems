"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Catalan Numbers
Link: https://open.kattis.com/contests/uaitfj/problems/catalan

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Combinatorics

Status: Accepted
Runtime: 1.24s
"""

import math


def calc_catalan_no(number: int) -> int:
    return math.comb(2 * number, number) - math.comb(2 * number, number + 1)


for _ in range(int(input())):
    print(calc_catalan_no(int(input())))
