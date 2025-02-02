"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Relocation
Link: https://open.kattis.com/contests/v499w5/problems/relocation

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.11s
"""

company_amount, request_amount = map(int, input().split(" "))
locations = list(map(int, input().split(" ")))

results = []

for _ in range(request_amount):
    req_type, first_arg, second_arg = map(int, input().split(" "))
    if req_type == 1:
        locations[first_arg - 1] = second_arg
    elif req_type == 2:
        results.append(abs(locations[first_arg - 1] - locations[second_arg - 1]))

[print(result) for result in results]
