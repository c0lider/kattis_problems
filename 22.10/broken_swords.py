"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Broken Swords
Link: https://open.kattis.com/contests/v499w5/problems/brokenswords

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.10s
"""

# TBLR
amount = int(input())
tb_amount = 0
rl_amount = 0

for _ in range(amount):
    t, b, l, r = input()
    tb_amount += (not int(t)) + (not int(b))
    rl_amount += (not int(r)) + (not int(l))

sword_amount = min((tb_amount, rl_amount)) // 2
tb_amount -= 2 * sword_amount
rl_amount -= 2 * sword_amount

print(f"{sword_amount} {tb_amount} {rl_amount}")
