"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Minimum Spanning Tree
Link: https://open.kattis.com/contests/m68tjy/problems/minspantree

@author Oliver Seiffermann
@version 4.0, 02/01/2024

Method: Minimum Spanning Tree

Status: Not Accepted - Run-Time Error
Runtime: 0.06s
"""

# TODO: Some kind or run-time error occurs in kattis...

from collections import defaultdict
from typing import List, Tuple


def is_connected(nodes, edges):
    adjecency_dict = defaultdict(list)
    for source_node, target_node, _ in edges:
        adjecency_dict[source_node].append(target_node)
        adjecency_dict[target_node].append(source_node)

    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in adjecency_dict[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(nodes[0])

    return len(visited) == len(nodes)


def find(parents: List, node: int):
    if parents[node] != node:
        parents[node] = find(parents, parents[node])
    return parents[node]


def union(parents: List, rank: List, first_node: int, target_node: int):
    if rank[first_node] < rank[target_node]:
        parents[first_node] = target_node
    elif rank[first_node] > rank[target_node]:
        parents[target_node] = first_node
    else:
        parents[target_node] = first_node
        rank[first_node] += 1


def calculate_mst(nodes: List, edges: Tuple[int, int, int]):
    parents = nodes[:]
    rank = [0] * len(nodes)

    mst_edges = []

    edges = sorted(edges, key=lambda item: item[2])
    current_edge_index = 0

    while len(mst_edges) < (len(nodes) - 1):
        curr_source, curr_target, weight = edges[current_edge_index]
        current_edge_index += 1

        source_root = find(parents, curr_source)
        target_root = find(parents, curr_target)

        if source_root != target_root:
            mst_edges.append((curr_source, curr_target, weight))
            union(parents, rank, source_root, target_root)

    return mst_edges


while True:
    amount_nodes, amount_edges = list(map(int, input().split()))

    if amount_nodes == 0 and amount_edges == 0:
        break

    # graph can not be connected in this case
    if amount_edges < (amount_nodes - 1):
        print("Impossible")
        continue

    nodes = list(range(amount_nodes))
    edges = []

    for _ in range(amount_edges):
        edges.append(tuple(map(int, input().split())))

    if not is_connected(nodes, edges):
        print("Impossible")
        continue

    mst_edges = sorted(calculate_mst(nodes, edges))
    total_cost = sum(edge[2] for edge in mst_edges)

    print(total_cost)
    [print(source, target) for source, target, _ in mst_edges]
