
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            distance = (p[0]**2 + p[1]**2)**.5
            heapq.heappush(heap, (-distance, p))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for h in heap:
            result.append(h[1])
        return result
