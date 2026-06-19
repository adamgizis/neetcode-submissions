import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter()
        for val in nums:
            c[val]+=1
        heap = []
        for val, freq in c.items():
            heapq.heappush(heap, (-1*freq, val))

        result = [heapq.heappop(heap)[1] for _ in range(min(k, len(heap)))]
        
        return result