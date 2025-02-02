"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Goldbach's Conjecture
Link: https://open.kattis.com/contests/acee7h/problems/goldbach2

@author Oliver Seiffermann
@version 5.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.14s
"""


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


amount_cases = int(input())
numbers = []
prime_representations = {}

for _ in range(amount_cases):
    numbers.append(int(input()))

for number in numbers:
    for factor in range(int(number / 2) + 1):
        if is_prime(factor) and is_prime(number - factor):
            try:
                prime_representations[number].append(f"{factor}+{number - factor}")
            except KeyError:
                prime_representations[number] = [f"{factor}+{number - factor}"]

for number, representations in prime_representations.items():
    print(f"{number} has {len(representations)} representation(s)")
    [print(representation) for representation in representations]
    print()
