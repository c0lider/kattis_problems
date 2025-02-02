"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Jack-O'-Lantern Juxtaposition
Link: https://open.kattis.com/contests/v499w5/problems/jackolanternjuxtaposition

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.04s
"""

numbers = [int(number) for number in input().split(" ")]

product = 1
for number in numbers:
    product *= number

print(product)
