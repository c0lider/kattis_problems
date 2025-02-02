"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Older Brother
Link: https://open.kattis.com/contests/acee7h/problems/olderbrother

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.04s
"""


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


number = int(input())

if len(set(prime_factors(number))) == 1:
    print("yes")
else:
    print("no")
