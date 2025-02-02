"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: How many Digits?
Link: https://open.kattis.com/contests/acee7h/problems/howmanydigits

@author Oliver Seiffermann
@version 2.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.05s
"""

import sys
from math import log10, pi, e


def estimate_digits(number: int):
    if number == 0:
        return 1
    return 1 + int(
        0.5 * (log10(2) + log10(pi))
        + 0.5 * log10(number)
        + number * (log10(number) - log10(e))
    )


numbers = []

for line in sys.stdin:
    numbers.append(int(line))

for number in numbers:
    print(estimate_digits(number))
