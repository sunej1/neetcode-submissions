import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        queue = []
        for stone in stones:
            heapq.heappush(queue, stone * (-1))
        while len(queue) >= 2:
            stone1 = heapq.heappop(queue)
            stone2 = heapq.heappop(queue)
            if stone1 > stone2:
                heapq.heappush(queue, stone2-stone1)
            elif stone1 < stone2:
                heapq.heappush(queue, stone1-stone2)
        if len(queue) > 0:
            return queue[0]*(-1)
        else:
            return 0