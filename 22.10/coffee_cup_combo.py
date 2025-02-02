"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Coffee Cup Combo
Link: https://open.kattis.com/contests/v499w5/problems/coffeecupcombo

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.05s
"""

input()
lectures = input()

awake_count = 0
amount_coffee = 0

for lecture in lectures:
    if lecture == "1":
        amount_coffee = 2
        awake_count += 1
    elif lecture == "0":
        if amount_coffee > 0:
            amount_coffee -= 1
            awake_count += 1

print(awake_count)
