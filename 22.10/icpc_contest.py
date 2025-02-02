"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: ICPC Awards
Link: https://open.kattis.com/contests/v499w5/problems/icpcawards

@author Oliver Seiffermann
@version 2.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.04s
"""

amount = int(input())

university_dict = {}

for index in range(amount):
    uni, team = input().split(" ")
    if university_dict.get(uni):
        continue
    university_dict[uni] = team

count = 0
for uni, team in university_dict.items():
    if (count := count + 1) <= 2:
        print(f"{uni} {team}")
