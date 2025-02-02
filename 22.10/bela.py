"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Bela 
Link: https://open.kattis.com/contests/v499w5/problems/bela

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.04s
"""

dominant_points = {"A": 11, "K": 4, "Q": 3, "J": 20, "T": 10, "9": 14, "8": 0, "7": 0}

non_dom_points = {"A": 11, "K": 4, "Q": 3, "J": 2, "T": 10, "9": 0, "8": 0, "7": 0}

no_hands, trump = input().split(" ")
no_hands = int(no_hands)

points = 0

for _ in range(4 * no_hands):
    card, suit = input()
    if suit == trump:
        points += dominant_points[card]
    else:
        points += non_dom_points[card]

print(points)
