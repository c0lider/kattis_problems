"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Pea Soup and Pancakes
Link: https://open.kattis.com/contests/v499w5/problems/peasoup

@author Oliver Seiffermann
@version 4.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.04s
"""


def handle_restaurant():
    item_amount = int(input())
    restaurant_name = input()
    items = []

    for _ in range(item_amount):
        items.append(input())

    if "pea soup" in items and "pancakes" in items:
        return restaurant_name
    else:
        return ""


amount = int(input())
result_name = ""

for _ in range(amount):
    resturant_name = handle_restaurant()
    if not result_name and resturant_name:
        result_name = resturant_name

if result_name:
    print(result_name)
else:
    print("Anywhere is fine I guess")
