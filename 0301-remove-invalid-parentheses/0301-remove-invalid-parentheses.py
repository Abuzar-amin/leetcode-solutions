class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left = right = 0

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left:
                    left -= 1
                else:
                    right += 1

        ans = set()

        def dfs(i, path, balance, lremove, rremove):
            if i == len(s):
                if balance == 0 and lremove == 0 and rremove == 0:
                    ans.add(''.join(path))
                return

            ch = s[i]

            if ch == '(' and lremove:
                dfs(i + 1, path, balance, lremove - 1, rremove)

            if ch == ')' and rremove:
                dfs(i + 1, path, balance, lremove, rremove - 1)

            path.append(ch)

            if ch == '(':
                dfs(i + 1, path, balance + 1, lremove, rremove)
            elif ch == ')':
                if balance:
                    dfs(i + 1, path, balance - 1, lremove, rremove)
            else:
                dfs(i + 1, path, balance, lremove, rremove)

            path.pop()

        dfs(0, [], 0, left, right)
        return list(ans)