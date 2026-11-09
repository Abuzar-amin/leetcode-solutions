from sortedcontainers import SortedList
import heapq
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            while busy and busy[0][0] <= time:
                finish, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            idx = available.bisect_left(i % k)

            if idx == len(available):
                idx = 0

            server = available.pop(idx)
            count[server] += 1

            heapq.heappush(busy, (time + load[i], server))

        highest = max(count)

        return [i for i in range(k) if count[i] == highest]
