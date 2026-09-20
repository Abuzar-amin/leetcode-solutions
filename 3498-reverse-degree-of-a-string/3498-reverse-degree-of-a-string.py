class Solution:
    def reverseDegree(self, s: str) -> int:
        mapping = {chr(i): 26 - (i - ord('a')) for i in range(ord('a'), ord('z') + 1)}
        sum = 0
        for i, char in enumerate(s,1):
            sum += mapping[char] * i
        return sum