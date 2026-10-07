class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans = []

        def remove(s, start, last, par):
            balance = 0

            for i in range(start, len(s)):
                if s[i] == par[0]:
                    balance += 1
                elif s[i] == par[1]:
                    balance -= 1

                if balance >= 0:
                    continue

                for j in range(last, i + 1):
                    if s[j] == par[1] and (j == last or s[j - 1] != par[1]):
                        remove(
                            s[:j] + s[j + 1:],
                            i,
                            j,
                            par
                        )
                return

            s = s[::-1]

            if par[0] == '(':
                remove(s, 0, 0, ')(')
            else:
                ans.append(s)

        remove(s, 0, 0, '()')
        return ans