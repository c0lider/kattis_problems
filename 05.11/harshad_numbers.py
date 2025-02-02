"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Harshad's Numbers
Link: https://open.kattis.com/contests/acee7h/problems/harshadnumbers

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.04s
"""


def digit_sum(number: int):
    total = 0
    while number > 0:
        total = total + number % 10
        number //= 10

    return total


def is_harshad(number: int):
    return number % digit_sum(number) == 0


number = int(input())

while not is_harshad(number):
    number += 1

print(number)
