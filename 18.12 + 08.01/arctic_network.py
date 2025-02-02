"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Arctic Network
Link: https://open.kattis.com/contests/m68tjy/problems/arcticnetwork

@author Oliver Seiffermann
@version 2.0, 02/01/2024

Method: Minimum Spanning Tree

Status: Not Accepted - Wrong Answer
Runtime: 0.82s
"""

# TODO: Wrong answer but should actually work...


from typing import List, Tuple
import math


def get_distance(source: Tuple[int, int], target: Tuple[int, int]) -> float:
    # basic Euclidean distance
    return math.sqrt((source[0] - target[0]) ** 2 + (source[1] - target[1]) ** 2)


def calculate_mst(coordinates: List[Tuple[int, int]]) -> List[float]:
    num_coordinates = len(coordinates)
    edges = []

    for i in range(num_coordinates):
        for j in range(i + 1, num_coordinates):
            distance = get_distance(coordinates[i], coordinates[j])
            edges.append((distance, i, j))

    edges.sort()

    # use kruskal algorithm
    parent = list(range(num_coordinates))
    rank = [0] * num_coordinates

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(first_node, second_node):
        first_node_root = find(first_node)
        second_node_root = find(second_node)

        if first_node_root != second_node_root:
            if rank[first_node_root] > rank[second_node_root]:
                parent[second_node_root] = first_node_root
            elif rank[first_node_root] < rank[second_node_root]:
                parent[first_node_root] = second_node_root
            else:
                parent[second_node_root] = first_node_root
                rank[first_node_root] += 1

    mst_weights = []

    for weight, source_node, target_node in edges:
        if find(source_node) != find(target_node):
            union(source_node, target_node)
            mst_weights.append(weight)

    return mst_weights


amount_tests = int(input())

for _ in range(amount_tests):
    satellite_channels, amount_outposts = map(int, input().split())
    coords = [tuple(map(int, input().split())) for _ in range(amount_outposts)]

    mst_weights = calculate_mst(coords)

    mst_weights.sort(reverse=True)
    max_radio_distance = mst_weights[satellite_channels - 1]

    print(round(max_radio_distance, 2))
