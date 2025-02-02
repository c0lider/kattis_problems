"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Fundamental Neighbors
Link: https://open.kattis.com/contests/acee7h/problems/fundamentalneighbors

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Number Theory

Status: Accepted 
Runtime: 0.30s
"""

import sys


def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2

    if n > 2:
        factors.append(n)

    return factors


def get_fundamental_neighbor(factors_dict: dict):
    total = 1
    for factor, exponent in factor_dict.items():
        total *= exponent**factor

    return total


numbers = []

for line in sys.stdin:
    numbers.append(int(line))

for number in numbers:
    factors = prime_factors(number)
    factor_dict = {}
    for factor in set(factors):
        factor_dict[factor] = factors.count(factor)

    print(f"{number} {get_fundamental_neighbor(factor_dict)}")
