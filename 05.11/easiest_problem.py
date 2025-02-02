"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: The easiest problem is this one
Link: https://open.kattis.com/contests/acee7h/problems/easiest

@author Oliver Seiffermann
@version 2.0, 02/01/2024

Method: Ad-Hoc 

Status: Accepted 
Runtime: 0.06s
"""


def sum_of_digits(number: int):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10

    return total


def find_p(number: int):
    sum_of_digits_of_N = sum_of_digits(number)
    p = 11
    while 1:
        if sum_of_digits(number * p) == sum_of_digits_of_N:
            return p

        p += 1


numbers = []
while (number := int(input())) != 0:
    numbers.append(find_p(number))

for number in numbers:
    print(number)
