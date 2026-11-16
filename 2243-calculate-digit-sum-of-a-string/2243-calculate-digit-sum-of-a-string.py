class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            result = []

            for i in range(0, len(s), k):
                group_sum = sum(int(digit) for digit in s[i:i + k])
                result.append(str(group_sum))

            s = ''.join(result)

        return s
