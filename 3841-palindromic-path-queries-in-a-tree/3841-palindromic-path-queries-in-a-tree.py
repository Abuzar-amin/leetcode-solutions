class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, value):
        i += 1
        while i <= self.n:
            self.tree[i] ^= value
            i += i & -i

    def query(self, i):
        result = 0
        while i > 0:
            result ^= self.tree[i]
            i -= i & -i
        return result


class Solution:
    def palindromePath(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

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

            for child in reversed(graph[node]):
                if child != par:
                    depth[child] = depth[node] + 1
                    stack.append((child, node, False))

        levels = n.bit_length()
        up = [parent[:]]

        for j in range(1, levels):
            previous = up[-1]
            up.append([previous[previous[i]] for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            difference = depth[u] - depth[v]
            bit = 0

            while difference:
                if difference & 1:
                    u = up[bit][u]
                difference >>= 1
                bit += 1

            if u == v:
                return u

            for j in range(levels - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        chars = [1 << (ord(c) - ord('a')) for c in s]
        tree = FenwickTree(n)

        for node in range(n):
            tree.update(tin[node], chars[node])
            tree.update(tout[node], chars[node])

        ans = []

        for query in queries:
            parts = query.split()
            op = parts[0]
            u = int(parts[1])

            if op == "update":
                new_char = 1 << (ord(parts[2]) - ord('a'))
                change = chars[u] ^ new_char

                if change:
                    tree.update(tin[u], change)
                    tree.update(tout[u], change)
                    chars[u] = new_char

            else:
                v = int(parts[2])
                ancestor = lca(u, v)

                mask = (
                    tree.query(tin[u] + 1)
                    ^ tree.query(tin[v] + 1)
                    ^ chars[ancestor]
                )

                ans.append((mask & (mask - 1)) == 0)

        return ans
