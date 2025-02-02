"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Sauna
Link: https://open.kattis.com/contests/p6fq6m/problems/sauna

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted
Runtime: 0.13s
"""

amount_people = int(input())
preferences = []

min_temp, max_temp = 0, 200_000

for _ in range(amount_people):
    curr_min, curr_max = map(int, input().split(" "))
    if curr_min > min_temp:
        min_temp = curr_min
    if curr_max < max_temp:
        max_temp = curr_max

if min_temp > max_temp:
    print("bad news")
else:
    possible_temps_amount = max_temp - min_temp + 1
    print(possible_temps_amount, min_temp, sep=" ")
