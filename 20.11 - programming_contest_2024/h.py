"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: A Stack of Gold
Link: https://open.kattis.com/contests/p6fq6m/problems/astackofgold

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted
Runtime: 0.04s
"""

GOLD_COIN_WEIGHT = 29_370
TUNGSTEN_COIN_WEIGHT = 29_260

total_weight, no_stacks = map(int, input().split(" "))

for stack in range(1, no_stacks + 1):
    if (total_weight - stack * GOLD_COIN_WEIGHT) % TUNGSTEN_COIN_WEIGHT == 0:
        print(stack)
