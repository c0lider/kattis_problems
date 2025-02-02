"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Which number kind is it?
Link: https://open.kattis.com/contests/p6fq6m/problems/whichnumberkindisit2

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted
Runtime: 0.28s
"""

amount = int(input())

for _ in range(amount):
    is_odd = False
    is_sqrt = False

    curr_no = int(input())

    if curr_no % 2 != 0:
        is_odd = True
        print("O", end="")

    if curr_no ** (1 / 2) % 1 == 0:
        is_sqrt = True
        print("S", end="")

    if not is_sqrt and not is_odd:
        print("EMPTY", end="")

    print()
