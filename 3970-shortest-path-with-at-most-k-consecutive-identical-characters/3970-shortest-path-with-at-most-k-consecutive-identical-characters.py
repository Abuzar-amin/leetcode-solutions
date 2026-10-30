import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][run] = minimum cost to reach node
        # with 'run' consecutive identical characters
        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        dist[0][1] = 0

        pq = [(0, 0, 1)]

        while pq:
            cost, node, run = heapq.heappop(pq)

            if cost != dist[node][run]:
                continue

            if node == n - 1:
                return cost

            for neighbor, weight in graph[node]:
                if labels[neighbor] == labels[node]:
                    new_run = run + 1
                else:
                    new_run = 1

                if new_run > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[neighbor][new_run]:
                    dist[neighbor][new_run] = new_cost
                    heapq.heappush(
                        pq, (new_cost, neighbor, new_run)
                    )

        return -1
