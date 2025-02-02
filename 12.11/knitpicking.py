"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Knitpicking
Link: https://open.kattis.com/contests/iju6a9/problems/knitpicking

@author Oliver Seiffermann
@version 2.0, 02/01/2024

Method: Ad-Hoc 

Status: Not Accepted - Wrong Answer
Runtime: 0.05s
"""

amount = int(input())

sock_data = []

for _ in range(amount):
    sock_data.append(input().split())

sock_types = {}

for sock_type, fit, count in sock_data:
    if sock_type not in sock_types:
        sock_types[sock_type] = {"left": 0, "right": 0, "any": 0}

    sock_types[sock_type][fit] += int(count)

total_draws = 0
possible_to_pair = False

for fits in sock_types.values():
    left_count = fits["left"]
    right_count = fits["right"]
    any_count = fits["any"]

    if (
        (left_count > 0 and right_count > 0)
        or (left_count > 0 and any_count > 0)
        or (right_count > 0 and any_count > 0)
    ):

        total_draws += max(left_count, right_count)
        possible_to_pair = True
    elif any_count > 1:
        total_draws += 1
        possible_to_pair = True
    else:
        continue

if possible_to_pair:
    print(total_draws + 1)
else:
    print("impossible")
