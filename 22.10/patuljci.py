"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Patuljci
Link: https://open.kattis.com/contests/v499w5/problems/patuljci

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.04s
"""

from itertools import combinations

numbers = set()

for _ in range(9):
    numbers.add(int(input()))

for combination in combinations(numbers, 7):
    if sum(combination) == 100:
        [print(number) for number in combination]
        break
