"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: 4 Thought
Link: https://open.kattis.com/contests/uaitfj/problems/4thought

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Precompute Solutions 

Status: Accepted
Runtime: 0.04s
"""

operators = ["+", "-", "*", "/"]


def evaluate_expression(expression):
    try:
        result = eval(expression.replace("/", "//"))
        return result
    except ZeroDivisionError:
        return None


def generate_expressions():
    expressions = set()
    for op1 in operators:
        for op2 in operators:
            for op3 in operators:
                expressions.add(f"4 {op1} 4 {op2} 4 {op3} 4")

    return expressions


def precompute_solutions():
    solution_map = {}
    expressions = generate_expressions()
    for expr in expressions:
        result = evaluate_expression(expr)
        if result is not None and result not in solution_map:
            solution_map[result] = expr
    return solution_map


def solve_test_cases(test_cases, solution_map):
    results = []
    for target in test_cases:
        if target in solution_map:
            results.append(solution_map[target] + f" = {target}")
        else:
            results.append("no solution")
    return results


num_cases = int(input())
test_cases = []

for _ in range(num_cases):
    test_cases.append(int(input()))

solution_map = precompute_solutions()

results = solve_test_cases(test_cases, solution_map)

for result in results:
    print(result)
