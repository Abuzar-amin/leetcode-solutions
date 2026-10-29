from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]],
                       s: str, queries: List[str]) -> List[bool]:

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Build Euler tour without recursion
        stack = [(0, 0, False)]

        while stack:
            node, par, exiting = stack.pop()

            if exiting:
                tout[node] = timer
                continue

            parent[node] = par
            tin[node] = timer
            timer += 1

            stack.append((node, par, True))

            for child in graph[node]:
                if child != par:
                    depth[child] = depth[node] + 1
                    stack.append((child, node, False))

        # Binary lifting for LCA
        levels = n.bit_length()
        up = [parent[:]]

        for j in range(1, levels):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for j in range(levels - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        # Fenwick tree with XOR
        bit = [0] * (n + 1)

        def add(index, value):
            index += 1
            while index <= n:
                bit[index] ^= value
                index += index & -index

        def prefix(index):
            result = 0
            index += 1

            while index > 0:
                result ^= bit[index]
                index -= index & -index

            return result

        def update_subtree(node, change):
            add(tin[node], change)

            if tout[node] < n:
                add(tout[node], change)

        chars = [1 << (ord(c) - ord('a')) for c in s]

        for node in range(n):
            update_subtree(node, chars[node])

        answer = []

        for query in queries:
            parts = query.split()
            u = int(parts[1])

            if parts[0] == "update":
                new_char = 1 << (ord(parts[2]) - ord('a'))
                change = chars[u] ^ new_char

                if change:
                    update_subtree(u, change)
                    chars[u] = new_char

            else:
                v = int(parts[2])
                ancestor = lca(u, v)

                mask = (
                    prefix(tin[u])
                    ^ prefix(tin[v])
                    ^ chars[ancestor]
                )

                answer.append((mask & (mask - 1)) == 0)

        return answer
