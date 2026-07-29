import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for v in stones:
            heapq.heappush(heap, -v)

        while heap:
            val1 = -heapq.heappop(heap)
            val2 = None
            if heap:
                val2 = -heapq.heappop(heap)
            else:
                return val1
            if val1-val2 > 0:
                heapq.heappush(heap, -(val1-val2))

        return 0
            