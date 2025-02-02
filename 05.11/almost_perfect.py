"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Almost Perfect
Link: https://open.kattis.com/contests/acee7h/problems/almostperfect

@author Oliver Seiffermann
@version 8.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.06s
"""

import sys
from math import sqrt


def get_divisors(number: int):
    divisors = []
    for factor in range(1, int(sqrt(number)) + 1):
        if number % factor == 0:
            if number != factor:
                divisors.append(factor)
            if factor != number // factor:
                divisors.append(number // factor)

    divisors.remove(number)

    return divisors


numbers = []

for line in sys.stdin:
    numbers.append(int(line))

# while (number := input()) != '':
#     numbers.append(int(number))

for number in numbers:
    number = int(number)
    total_of_divisors = sum(get_divisors(number))
    if total_of_divisors == number:
        print(f"{number} perfect")
    elif abs(total_of_divisors - number) <= 2:
        print(f"{number} almost perfect")
    else:
        print(f"{number} not perfect")
