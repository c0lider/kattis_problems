"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Perfect Pth Power
Link: https://open.kattis.com/contests/acee7h/problems/perfectpowers

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Ad-Hoc 

Status: Not Accepted - Wrong Answer 
Runtime: 0.04s
"""


def get_perfect_pth(number: int):
    for factor in range(2, number):
        exponent = 2
        while factor**exponent <= number:
            if factor**exponent == number:
                return exponent
        exponent += 1

    return 1


numbers = []

while (number := int(input())) != 0:
    numbers.append(get_perfect_pth(number))

for number in numbers:
    print(number)
