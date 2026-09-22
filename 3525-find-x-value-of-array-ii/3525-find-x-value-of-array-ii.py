class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # tree[node] = [product % k, count[0], ..., count[k-1]]
        tree = [[1] + [0] * k for _ in range(4 * n)]

        def merge(a, b):
            prod = a[0] * b[0] % k
            cnt = a[1:].copy()

            for r in range(k):
                cnt[(a[0] * r) % k] += b[r + 1]

            return [prod] + cnt

        def build(node, l, r):
            if l == r:
                v = nums[l] % k
                tree[node] = [v] + [1 if i == v else 0 for i in range(k)]
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, pos, val):
            if l == r:
                v = val % k
                tree[node] = [v] + [1 if i == v else 0 for i in range(k)]
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(node * 2, l, mid, pos, val)
            else:
                update(node * 2 + 1, mid + 1, r, pos, val)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def query(node, l, r, ql):
            if ql <= l:
                return tree[node]

            mid = (l + r) // 2

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql)

            left = query(node * 2, l, mid, ql)
            right = query(node * 2 + 1, mid + 1, r, ql)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            res = query(1, 0, n - 1, start)

            ans.append(res[x + 1])

        return ans