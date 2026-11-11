class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        common = min(need1, need2)

        return min(
            need1 * cost1 + need2 * cost2,
            common * costBoth + (need1 - common) * cost1 + (need2 - common) * cost2,
            max(need1, need2) * costBoth
        )