"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Geppetto
Link: https://open.kattis.com/contests/iju6a9/problems/geppetto

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Not Accepted - Time Limit Exceeded
Runtime: >1.0s
"""

from itertools import combinations

no_ingredients, no_forbidden_combinations = map(int, input().split())
forbidden_combinations = set()

for _ in range(no_forbidden_combinations):
    a, b = map(int, input().split())
    forbidden_combinations.add((min(a, b), max(a, b)))

valid_pizzas = 0

for size in range(1, no_ingredients + 1):
    for subset in combinations(range(1, no_ingredients + 1), size):
        is_valid = True
        for a, b in combinations(subset, 2):
            if (min(a, b), max(a, b)) in forbidden_combinations:
                is_valid = False
                break
        if is_valid:
            valid_pizzas += 1

print(valid_pizzas + 1)
