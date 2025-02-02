"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025
Problem: Big Truck
Link: https://open.kattis.com/contests/m68tjy/problems/bigtruck

@author Oliver Seiffermann
@version 1.0, 02/01/2024

Method: Dijkstra

Status: Accepted
Runtime: 0.10s
"""

import heapq
from collections import defaultdict


class Graph:
    def __init__(self, no_edges):
        self.no_edges = no_edges
        self.edges = defaultdict(list)
        self.packages = [0] * (self.no_edges + 1)
        self.shortest = float("inf")
        self.package_sum = 0

    def read_packages(self):
        self.packages[1:] = map(int, input().split())

    def read_edges(self):
        for _ in range(int(input())):
            a, b, d = map(int, input().split())
            self.edges[a].append((b, d))
            self.edges[b].append((a, d))

    def possible(self):
        return self.shortest != float("inf")

    def search(self):
        # priority queue of (cost, -packages, edge)
        priority_queue = [(0, -self.packages[1], 1)]
        visited = set()

        while priority_queue:
            cost, neg_packages, edge = heapq.heappop(priority_queue)

            if edge == self.no_edges:
                self.shortest = cost
                self.package_sum = -neg_packages
                return

            if edge in visited:
                continue
            visited.add(edge)

            for neighbor, weight in self.edges[edge]:
                if neighbor not in visited:
                    heapq.heappush(
                        priority_queue,
                        (
                            cost + weight,
                            neg_packages - self.packages[neighbor],
                            neighbor,
                        ),
                    )


no_edges = int(input())
graph = Graph(no_edges)
graph.read_packages()
graph.read_edges()
graph.search()

if graph.possible():
    print(graph.shortest, graph.package_sum)
else:
    print("impossible")
