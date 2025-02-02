"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Veci
Link: https://open.kattis.com/contests/acee7h/problems/veci

@author Oliver Seiffermann
@version 2.0, 02/01/2024

Method: Ad-Hoc 

Status: Not Accepted - Wrong Answer 
Runtime: 0.04s
"""

from itertools import permutations


def get_permutations(s):
    return ["".join(p) for p in permutations(s)]


number_str = input()
potential_numbers = [
    perm for perm in get_permutations(number_str) if int(perm) > int(number_str)
]
if potential_numbers:
    print(min(potential_numbers))
else:
    print(0)
