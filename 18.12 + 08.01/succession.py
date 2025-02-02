"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Succession
Link: https://open.kattis.com/contests/m68tjy/problems/succession

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Recursion

Status: Accepted
Runtime: 0.04s
"""


def calculate_blood_value(child: str) -> float:
    if child == founder:
        return 1
    else:
        try:
            first_parent, second_parent = parents[child]
            return (
                calculate_blood_value(first_parent)
                + calculate_blood_value(second_parent)
            ) / 2
        except KeyError:
            # child is no direct descendant
            return 0


amount_family_relations, amount_claimants = map(int, input().split())
founder = input()

parents = {}
for _ in range(amount_family_relations):
    child, first_parent, second_parent = input().split()
    parents[child] = (first_parent, second_parent)

claimants = {}
for _ in range(amount_claimants):
    claimants[input()] = 0

blood_values = {}
for claimant in claimants:
    blood_values[claimant] = calculate_blood_value(claimant)

print(max(blood_values, key=blood_values.get))
