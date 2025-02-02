"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Minimal Fibonacci Sums
Link: https://open.kattis.com/contests/rfq9ju/problems/fibonaccisum

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Greedy Algorithm using the "Zeckendorf representation"

Status: Accepted
Runtime: 0.04s
"""


def find_fibonacci_sum(n):
    fib = [1, 2]

    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])

    if fib[-1] > n:
        fib.pop()

    result = []
    while n > 0:

        for i in range(len(fib) - 1, -1, -1):
            if fib[i] <= n:
                result.append(fib[i])
                n -= fib[i]
                break

    return sorted(result)


n = int(input())
result = find_fibonacci_sum(n)
print(" ".join(map(str, result)))
