"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Breaking Bad
Link: https://open.kattis.com/contests/m68tjy/problems/breakingbad

@author Oliver Seiffermann
@version 2.0, 02/01/2024

Method: Graph Bipartiteness Check with BFS

Status: Accepted
Runtime: 0.20s
"""

from collections import defaultdict, deque


def split_graph(adjacency_list: dict) -> dict:
    colors = {}
    queue = deque()

    for node in adjacency_list:
        if node not in colors:
            queue.append(node)
            colors[node] = 0

            while queue:
                current_node = queue.popleft()
                current_color = colors[current_node]

                for neighbor in adjacency_list[current_node]:
                    if neighbor not in colors:
                        colors[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif colors[neighbor] == current_color:
                        return {}

    return colors


amount_items = int(input())
items = [input() for _ in range(amount_items)]

amount_forbidden_combinations = int(input())
forbidden_combinations = defaultdict(set)

for _ in range(amount_forbidden_combinations):
    first_item, second_item = input().split()
    forbidden_combinations[first_item].add(second_item)
    forbidden_combinations[second_item].add(first_item)

for item in items:
    if item not in forbidden_combinations:
        forbidden_combinations[item] = set()

split_items = split_graph(forbidden_combinations)

if not split_items:
    print("impossible")
else:
    walters_items = sorted(key for key, value in split_items.items() if value == 0)
    jesses_items = sorted(key for key, value in split_items.items() if value == 1)
    print(" ".join(walters_items))
    print(" ".join(jesses_items))
