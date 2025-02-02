"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Get Shorty
Link: https://open.kattis.com/contests/m68tjy/problems/getshorty

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: (modified) Dijkstra's Algorithm

Status: Not Accepted - Wrong answer
Runtime: 0.04s
"""

# TODO: Answer seems to be wrong..
import heapq
import math


def max_product_path(graph, start, end):
    # Find the path with the maximum product of weights in a graph.
    priority_queue = [(-math.log(1), start, [start])]
    visited = set()

    while priority_queue:
        neg_log_product, current, path = heapq.heappop(priority_queue)
        log_product = -neg_log_product

        if current in visited:
            continue

        visited.add(current)

        if current == end:
            max_product = math.exp(-log_product)
            return round(max_product, 4)

        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                new_log_product = log_product - math.log(weight)
                heapq.heappush(
                    priority_queue, (-new_log_product, neighbor, path + [neighbor])
                )

    return -1


while True:
    amount_nodes, amount_edges = map(int, input().split())
    if not amount_nodes and not amount_edges:
        break

    graph = {}

    for _ in range(amount_edges):
        source_node, target_node, weight = list(map(float, input().split()))
        source_node, target_node = int(source_node), int(target_node)

        if source_node not in graph:
            graph[source_node] = []
        if target_node not in graph:
            graph[target_node] = []

        graph[source_node].append((target_node, weight))
        graph[target_node].append((source_node, weight))

    print(max_product_path(graph, 0, amount_nodes - 1))
